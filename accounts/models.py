from django.db import models
from config.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profileimage = models.ImageField(upload_to="images/", blank=True)
    nickname = models.CharField(max_length=10, blank=True)
    refresh_token = models.TextField(blank=True)
    is_creater = models.BooleanField(default=False)
    location = models.CharField(max_length=40)
    location_detail = models.CharField(max_length=40)
    test = models.CharField(max_length=40, blank=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
