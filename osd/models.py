from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify


class Event(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=60, blank=True)
    date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.code = slugify(self.name)
        return super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=30)
    event = models.ForeignKey(Event)
    length = models.DurationField(blank=True, null=True)

class SpeakerBase(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=240)
    email = models.EmailField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    company = models.TextField(max_length=200, blank=True)
    title = models.CharField(max_length=30, blank=True)
    abstract = models.TextField(max_length=1000, blank=True)
    session = models.ForeignKey(Session)

class Proposal(SpeakerBase):
    accepted = models.BooleanField(default=False)

class Speaker(SpeakerBase):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_speaker(sender, instance, created, **kwargs):
    if created and hasattr(instance, 'speaker'):
        Speaker.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_speaker(sender, instance, **kwargs):
    if hasattr(instance, 'speaker'):
        instance.speaker.save()

class SponsorType(models.Model):
    name = models.CharField(max_length=30)

class Sponsor(models.Model):
    name = models.TextField(max_length=360)
    logo = models.CharField(max_length=60, blank=True)
    email = models.EmailField(blank=True)
    contact_name = models.CharField(max_length=120)
    sponsor_type = models.ForeignKey(SponsorType)
