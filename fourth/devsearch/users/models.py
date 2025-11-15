from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=500, blank=True)
    username = models.CharField(max_length=200, blank=True)
    short_intro = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True)
    social_youtube = models.CharField(max_length=200, blank=True)
    social_website = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def profile_update(sender, instance, created, **kwargs):
    print("Sender:", sender)
    print("Instance:", instance)
    print("Created:", created)


def delete_users(sender, instance, **kwargs):
    print("Deleting user...")


post_save.connect(profile_update, sender=Profile)
post_delete.connect(delete_users, sender=Profile)