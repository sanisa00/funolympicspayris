from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SPORTS_CATEGORIES = (
        ('ATHLETICS', 'Athletics'),
        ('AQUATICS', 'Aquatics'),
        ('COMBAT', 'Combat'),
        ('GYMNASTICS', 'Gymnastics'),
        ('SHOOTING', 'Shooting'),
        ('TEAM', 'Team'),
    )

    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    sports_category = models.CharField(max_length=20, choices=SPORTS_CATEGORIES, null=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    # host =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/events/image/', null=True, blank=True)
    video_url = models.FileField(upload_to='media/events_videos/', null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    



