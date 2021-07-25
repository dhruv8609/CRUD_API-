from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from accounts.models import *
# Create your models here.

from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


# This model contains only title and description field for VideoModel.Other fields such as FileField/UrlField
#		could be added to include more info of the lecture

class VideoModel(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(blank=True)
    attendees = models.TextField(default="")
    mentor = models.ManyToManyField(
        User)
    slug = models.SlugField(blank=False, unique=True)

    def __str__(self):
        return self.title


def pre_save_videomodel(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_videomodel, sender=VideoModel)

# , on_delete=models.SET_NULL, blank=True, null=True
