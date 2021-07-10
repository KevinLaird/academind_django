from django.db import models
from django.utils import timezone

# Create your models here.

class Organizer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.slug} - {self.location}'

