from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    country = models.TextField(max_length=100, blank=True, null=True)
    city = models.TextField(max_length=100, blank=True, null=True)
    phone_number = models.TextField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)

    created_on = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            instance.userprofile.save()

        post_save.connect(UserProfile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        UserProfile.objects.get_or_create(user=instance)
        instance.userprofile.save()

