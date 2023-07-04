from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.username