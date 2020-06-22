from django.db import models
from django.contrib.auth.models import User

class Leaderboard(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    good_first_issue = models.BooleanField(default=False) #Shall be true on completion of Good first issue
    medium_question_1 = models.BooleanField(default=False) #Shall be true on completion of first medium issue
    medium_question_2 = models.BooleanField(default=False) #Shall be true on completion of first medium issue
    '''
    We can identify labels for various situations as follows
        1. good_start -> good_first_issue = True
                        medium_question_1 = False
                        medium_question_2 = False
        2. terrific_start -> good_first_issue = False
                        medium_question_1 = True
                        medium_question_2 = False
        3. almost_there -> good_first_issue = True
                        medium_question_1 = True
                        medium_question_2 = False
        4. mission_accomplished -> good_first_issue = True
                                    medium_question_1 = True
                                    medium_question_2 = True
    '''
