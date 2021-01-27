from django.db import models
from django.contrib.auth.models import User

class Leaderboard(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    good_first_issue = models.BooleanField(default=False) #Shall be true on completion of Good first issue
    milestone_achieved = models.BooleanField(default=False) #Shall be true on achieving milestone of 2 medium and 1 good first issue
    medium_issues_solved = models.IntegerField(default=0) # Count the number of medium issues solved.
    hard_issues_solved = models.IntegerField(default=0) # Count the number of hard issues solved.
    pr_opened = models.IntegerField(default=0) # Count the number of PRs opened.
    pr_merged = models.IntegerField(default=0) # Count the number of PRs merged.
    '''
    We can identify labels for various situations as follows
        1. good_start -> good_first_issue = True
                        medium_issues_solved = 0
        2. terrific_start -> good_first_issue = False
                        medium_issues_solved = 1
        3. almost_there -> good_first_issue = True
                        medium_issues_solved = 1
        4. mission_accomplished -> good_first_issue = True
                                    medium_issues_solved = 2
    '''
    def __str__(self):
        return self.username.username