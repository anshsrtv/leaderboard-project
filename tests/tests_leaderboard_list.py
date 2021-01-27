import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from profiles.models import Leaderboard

class LeaderboardListTestCase(APITestCase):
    '''
    This class is to test the pull_request view
    from profiles.views.py
    '''

    def setUp(self):
        '''creating a list of users and populating it
        with solved issues and points'''

        self.users = []
        self.leaderboards = []

        #Create Users and leaderboards
        for i in range(6):
            user = User.objects.create_user(
                email='test_user'+str(i)+'@gmail.com',
                username='testuser'+str(i),
                password='test_password'+str(i),
            )
            self.users.append(user)
            leaderboard_obj = Leaderboard.objects.create(
                username=user
            )
            self.leaderboards.append(leaderboard_obj)

        '''Populating them with various issues such that
        first member - Has solved no issues.
        second member onwards everbody has solved a good first issue.
        third member onwards everbody has solved a medium issue.
        fourth member onwards everbody has solved 2 medium issues.
        fifth member onwards everbody has solved a hard issue.'''
        for i in range(6):
            if i > 0:
                #All members except the one on index 0 solving a good first issue
                good_first_issue_payload = {
                    'action':'closed',
                    'issue':{
                        'labels':[
                            {
                                'name':'good first issue',
                            },
                        ],
                        'assignee':{
                            'login':self.leaderboards[i].username.username,
                            }
                        },
                    }
                response = self.client.post("/issue/", json.dumps(good_first_issue_payload),
                                            content_type="application/json")
            if i > 1:
                #All members except the one on index 0, 1 solving a medium issue
                medium_payload = {
                    'action':'closed',
                    'issue':{
                        'labels':[
                            {
                                'name':'medium',
                            },
                        ],
                        'assignee':{
                            'login':self.leaderboards[i].username.username,
                            }
                        },
                    }
                response = self.client.post("/issue/", json.dumps(medium_payload),
                                            content_type="application/json")

            if i > 2:
                #All members except the one on index 0, 1, 2 solving their second medium issue
                response = self.client.post("/issue/", json.dumps(medium_payload),
                                            content_type="application/json")

            if i > 3:
                #All members except the one on index 0, 1, 2, 3 solving a hard issue
                hard_payload = {
                    'action':'closed',
                    'issue':{
                        'labels':[
                            {
                                'name':'hard',
                            },
                        ],
                        'assignee':{
                            'login':self.leaderboards[i].username.username,
                            }
                        },
                    }
                response = self.client.post("/issue/", json.dumps(hard_payload),
                                            content_type="application/json")

    def test_success(self):
        response = self.client.get("/leaderboard/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Check that response contains all leaderboards from the db
        self.assertEqual(len(response.data), len(self.leaderboards))

        '''Check the element with smaller rank has greater points
        for all elements in the response object'''
        for i in range(len(response.data) - 1):
            self.assertGreaterEqual(response.data[i]['points'], response.data[i+1]['points'])
            self.assertGreaterEqual(response.data[i+1]['rank'], response.data[i]['rank'])


    def tearDown(self):
        self.users.clear()
        self.leaderboards.clear()
