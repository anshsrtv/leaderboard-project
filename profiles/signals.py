from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Leaderboard

@receiver(post_save, sender=User)
def create_leaderboard_obj(sender, instance=None, **kwargs):
    if kwargs['created']:
        try:
            leaderboard = Leaderboard(username = instance)
            leaderboard.save()
        except:
            pass
    