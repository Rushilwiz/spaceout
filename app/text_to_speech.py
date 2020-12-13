import re
import os
import sys
import time
import winsound
import webbrowser
import threading
from threading import Thread

from pywinauto import application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError

from google.cloud import speech
import pyaudio
from six.moves import queue

# Audio recording parameters
STREAMING_LIMIT = 240000
SAMPLE_RATE = 16000
CHUNK_SIZE = int(SAMPLE_RATE / 10)


def get_current_time():
    return int(round(time.time() * 1000))


class ResumableMicrophoneStream:

    def __init__(self, rate, chunk_size):
        self._rate = rate
        self.chunk_size = chunk_size
        self._num_channels = 1
        self._buff = queue.Queue()
        self.closed = True
        self.start_time = get_current_time()
        self.restart_counter = 0
        self.audio_input = []
        self.last_audio_input = []
        self.result_end_time = 0
        self.is_final_end_time = 0
        self.final_request_end_time = 0
        self.bridging_offset = 0
        self.last_transcript_was_final = False
        self.new_stream = True
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=self._num_channels,
            rate=self._rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            stream_callback=self._fill_buffer,
        )

    def __enter__(self):

        self.closed = False
        return self

    def __exit__(self, type, value, traceback):

        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, *args, **kwargs):

        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):

        while not self.closed:
            data = []

            if self.new_stream and self.last_audio_input:

                chunk_time = STREAMING_LIMIT / len(self.last_audio_input)

                if chunk_time != 0:

                    if self.bridging_offset < 0:
                        self.bridging_offset = 0

                    if self.bridging_offset > self.final_request_end_time:
                        self.bridging_offset = self.final_request_end_time

                    chunks_from_ms = round(
                        (self.final_request_end_time - self.bridging_offset)
                        / chunk_time
                    )

                    self.bridging_offset = round(
                        (len(self.last_audio_input) - chunks_from_ms) * chunk_time
                    )

                    for i in range(chunks_from_ms, len(self.last_audio_input)):
                        data.append(self.last_audio_input[i])

                self.new_stream = False

            chunk = self._buff.get()
            self.audio_input.append(chunk)

            if chunk is None:
                return
            data.append(chunk)
            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)

                    if chunk is None:
                        return
                    data.append(chunk)
                    self.audio_input.append(chunk)

                except queue.Empty:
                    break

            yield b"".join(data)


def listen_print_loop(responses, stream, name):
    for response in responses:

        if get_current_time() - stream.start_time > STREAMING_LIMIT:
            stream.start_time = get_current_time()
            break

        if not response.results:
            continue

        result = response.results[0]

        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript

        if result.is_final:
            sys.stdout.write("Final: " + transcript + "\n")

            stream.is_final_end_time = stream.result_end_time
            stream.last_transcript_was_final = True
            transcript_file = open("current_transcript", "a")
            transcript_file.write(f'{time.strftime("%H:%M:%S")} {transcript}\n')
            transcript_file.close()

            if re.search(r"\b("+ name + r")\b", transcript, re.IGNORECASE):
                name_called()
                stream.closed = True
                break

        else:
            sys.stdout.write("Speaking: " + transcript + "\r")

            stream.last_transcript_was_final = False


def name_called():
    for i in range(2):
        winsound.Beep(1500, 250)
        winsound.Beep(600, 250)

    app = application.Application()
    try:
        app.connect(title_re=".*Chrome.*")

        app_dialog = app.top_window()
        app_dialog.restore()
        app_dialog.maximize()

    except(WindowNotFoundError):
        print ("Couldn't open chrome")
        pass
    except(WindowAmbiguousError):
        print ('There are too many Chrome windows found')
        pass

    transcript = open('current_transcript', 'r')
    last_spoken = ''

    for line in (transcript.readlines()[-3:]): 
        last_spoken += line

    print(last_spoken)
    message_box(last_spoken)



def message_box (text):
    from PyQt5 import QtWidgets
    msg = QtWidgets.QMessageBox()
    msg.setText(text)
    msg.show()
    sys.exit(msg.exec_())

def text_to_speech(name):
    

    """start bidirectional streaming from microphone input to speech API"""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"SpaceOut.json"
    

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=SAMPLE_RATE,
        language_code="en-US",
        max_alternatives=1,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    mic_manager = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)

    with mic_manager as stream:

        while not stream.closed:

            stream.audio_input = []
            audio_generator = stream.generator()

            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            responses = client.streaming_recognize(streaming_config, requests)

            # Now, put the transcription responses to use.
            listen_print_loop(responses, stream, name)

            if stream.result_end_time > 0:
                stream.final_request_end_time = stream.is_final_end_time
            stream.result_end_time = 0
            stream.last_audio_input = []
            stream.last_audio_input = stream.audio_input
            stream.audio_input = []
            stream.restart_counter = stream.restart_counter + 1

            stream.new_stream = True
        
        listen_print_loop(responses, stream, name)

if __name__ == "__main__":
    text_to_speech("lucas") # just for testing if script is directly invoked
