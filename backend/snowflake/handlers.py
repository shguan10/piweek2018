from django.contrib.auth.models import User
from django.db.models.signals import post_save
from snowflake.fridge_viewset import Fridge


def save_profile(sender, instance, created, **kwargs):
    if created:
        Fridge.objects.create(user=sender)

post_save.connect(save_profile, sender=User)
