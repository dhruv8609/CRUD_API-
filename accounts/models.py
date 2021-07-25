from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from videocontent.models import VideoModel

class User(AbstractUser):

    class Types(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        MENTOR = "MENTOR", "Mentor"

    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=Types.STUDENT)

    email = models.EmailField(max_length=254, unique=True)
    # videomodel_id = models.ForeignKey(
    #     VideoModel, related_name='mentoruser', on_delete=models.CASCADE, null=True)

    # def get_absolute_url(self):
    #     return reverse("accounts:detail", kwargs={'pk'=self.pk})


class MentorManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.MENTOR)


class StudentManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)


class Mentor(User):
    objects = MentorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.MENTOR
            return super().save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
