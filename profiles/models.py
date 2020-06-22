from django.db import models
from django.contrib.auth.models import User

class Milestone(models.Model):
    good_start = models.BooleanField(default=False)
    terrific_start = models.BooleanField(default=False)
    almost_there = models.BooleanField(default=False)
    mission_accomplished = models.BooleanField(default=False)


class Leaderboard(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    milestones = models.ForeignKey(Milestone, on_delete=models.CASCADE)
