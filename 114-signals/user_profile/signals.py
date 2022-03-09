from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import UserProfile
from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(post_save, sender=User)
def user_post_save(sender, instance=None, created=False, **kwargs):
    if created:
        up = UserProfile(user=instance)
    else:
        up = UserProfile.objects.filter(user=instance).first()
    up.name = f'{instance.last_name}{instance.first_name}'
    up.save()


# @receiver(post_delete, sender=User)
# def user_post_delete(sender, instance=None, created=False, **kwargs):
#     up = UserProfile.objects.filter(user=instance).first()
#     up.delete()
