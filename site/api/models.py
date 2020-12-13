from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pic = models.ImageField(default='./api/media/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.profile_pic.path).convert('RGB')
    #
    #     if img.height > 300 or img.width > 300:
    #         size = (300, 300)
    #         img.thumbnail(size)
    #         img.save(self.profile_pic.path)


class Classroom(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)
    period = models.CharField(models.PositiveIntegerField, blank=True, unique=True, max_length=1)

    def __str__(self):
        return f"{self.student.user.username}'s Class: {self.name}"
