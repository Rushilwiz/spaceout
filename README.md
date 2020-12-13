<p align="center">
  <a href="https://github.com/rushilwiz/spaceout">
    <img src=".github/logo.png" alt="Logo" width=960px height=640px>
  </a>

  <h1 align="center">SpaceOut!</h1>

</p>

![GitHub language](https://img.shields.io/github/languages/top/rushilwiz/spaceout?color=FF6663)
![GitHub language count](https://img.shields.io/github/languages/count/rushilwiz/spaceout?color=FEB144)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rushilwiz/spaceout?color=FAFD7B)
![GitHub repo size](https://img.shields.io/github/repo-size/rushilwiz/spaceout?color=9EE09E)
![GitHub](https://img.shields.io/github/license/rushilwiz/spaceout?color=9EC1CF)
![GitHub last commit](https://img.shields.io/github/last-commit/rushilwiz/spaceout?color=CC99C9)

---

## Inspiration
As 2020 comes toward the end, people around the world have endured various struggles because of the coronavirus. Students around the world have been struggling to put full focus on academics during class and taking notes due to the online learning environment.

## What it does
**SpaceOut** uses speech to text features in python for your classes. The first function of SpaceOut is to record your class lectures using a streamed input device and write them down. The second feature of Space out is to notify a user when their name is called in class. Sometimes, students tend to space out, hence the name, during their classes because the online learning environment may not be as engaging as in-person learning. SpaceOut will notify a student anytime their name is called, and show the previous 50 words to the student in order for them to grasp an idea of what they are learning.

## How we built it
There were two parts to building SpaceOut. We built the website by using a Django server combined with the powerful Cockroach Database. In the website, we used the REST framework to create a secure API that our native desktop app used to get user information. After that, we had to configure a native desktop app to record and transcribe live audio data coming from the client's class/microphone.

## Challenges we ran into
We ran into many challenges during the development of this. One of the main challenges was creating the API backend using many serializers and the rest framework. The next challenge was to create a communication between the desktop app and the website, ensuring that there was no packet loss in the transmission. Also, we had trouble setting up the website server on our personal server using cloud flare and domain.com, but we were able to conquer this by having diligence.

## Accomplishments that we're proud of
We are extremely proud of the back and forth connections that we made between the website's API and the native desktop app. We are also proud of the clean UI that we made on the website. 

## What we learned
We have learned many things during this hackathon, including a new programming language. The main thing that we learned is that having big ideas for a small amount of time isn't good. Also, we have learned that there are detailed documentations for everything on the internet, and they will be extremely helpful. Lastly, we learned an entire framework (pyqt) in order to create the GUI which transcribes and saves audio.

## What's next for SpaceOut
Space out will continue to help with student needs and problems in an online environment. We want to ensure that students get a maximum learning experience and are able to stay focused during class, by creating efficient APIs and applications that assist them.
