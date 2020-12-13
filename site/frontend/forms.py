from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from api.models import Classroom


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
            self.fields[field].widget.attrs["class"] = "input100"


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ["name", "teacher", "link", "period"]

    def __init__(self, *args, **kwargs):
        super(ClassroomForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
            self.fields[field].widget.attrs["class"] = "input100"
