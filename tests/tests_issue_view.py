import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from profiles.models import Leaderboard


class IssueTestCase(APITestCase):
    '''
    This class is to test the issue view
    from profiles.views.py
    '''

    # Creating webhooks like payloads to test the views.

    good_first_issue_valid_payload = {
        'action':'closed',
        'issue':{
            'labels':[
                {
                    'name':'good first issue',
                },
            ],
            'assignee':{
                'login':'testuser',
            }
        },
    }

    medium_issue_valid_payload = {
        'action':'closed',
        'issue':{
            'labels':[
                {
                    'name':'medium',
                },
            ],
            'assignee':{
                'login':'testuser',
            }
        },
    }
    hard_issue_valid_payload = {
        'action':'closed',
        'issue':{
            'labels':[
                {
                    'name':'hard',
                },
            ],
            'assignee':{
                'login':'testuser',
            }
        },
    }

    hard_issue_invalid_user = {
        'action':'closed',
        'issue':{
            'labels':[
                {
                    'name':'hard',
                },
            ],
            'assignee':{
                'login':'invaliduser',
            }
        },
    }

    invalid_payload = {}

    def setUp(self):
        # Creating a test user and the corresponding leaderboard.
        self.user = User.objects.create_user(
            email='test_user@gmail.com',
            username='testuser',
            password='test_password',
        )

        self.leaderboard = Leaderboard.objects.get(
            username=self.user
        )

    def test_fail_invalid_payload(self):
        response = self.client.post("/issue/", json.dumps(self.invalid_payload),
                                    content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_success_with_solve_good_first_issue(self):
        # To check increment in points, we have prev_l_board and update_l_board.
        prev_l_board = Leaderboard.objects.get(username=self.user)

        response = self.client.post("/issue/", json.dumps(self.good_first_issue_valid_payload),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Check values
        updated_l_board = Leaderboard.objects.get(username=self.user)
        self.assertNotEqual(updated_l_board.good_first_issue, False)
        self.assertNotEqual(prev_l_board.points, updated_l_board.points)

    def test_success_with_solve_medium_issue(self):
        # To check increment in points, we have prev_l_board and update_l_board.
        prev_l_board = Leaderboard.objects.get(username=self.user)

        response = self.client.post("/issue/", json.dumps(self.medium_issue_valid_payload),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Check values
        updated_l_board = Leaderboard.objects.get(username=self.user)
        self.assertNotEqual(updated_l_board.medium_issues_solved, 0)
        self.assertNotEqual(prev_l_board.points, updated_l_board.points)


    def test_success_with_solve_hard_issue(self):
        # To check increment in points, we have prev_l_board and update_l_board.
        prev_l_board = Leaderboard.objects.get(username=self.user)

        response = self.client.post("/issue/", json.dumps(self.hard_issue_valid_payload),
                                    content_type="application/json")

        #Check values
        updated_l_board = Leaderboard.objects.get(username=self.user)
        self.assertNotEqual(updated_l_board.hard_issues_solved, 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(prev_l_board.points, updated_l_board.points)

    def test_success_with_milestone_achieved(self):
        '''The milestone is said to be achieved when one good first issue and two
        medium issues are solved. This tests checks the success in updation of the
        milestone_achieved field.'''
        # To check increment in points, we have prev_l_board and update_l_board.
        prev_l_board = Leaderboard.objects.get(username=self.user)

        #Solving one good first and two medium issues.
        response = self.client.post("/issue/", json.dumps(self.good_first_issue_valid_payload),
                                    content_type="application/json")
        response = self.client.post("/issue/", json.dumps(self.medium_issue_valid_payload),
                                    content_type="application/json")
        response = self.client.post("/issue/", json.dumps(self.medium_issue_valid_payload),
                                    content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Check values
        updated_l_board = Leaderboard.objects.get(username=self.user)
        self.assertGreaterEqual(updated_l_board.medium_issues_solved, 2)
        self.assertNotEqual(updated_l_board.good_first_issue, False)
        self.assertNotEqual(updated_l_board.milestone_achieved, False)
        self.assertNotEqual(prev_l_board.points, updated_l_board.points)

    def test_fail_invalid_user(self):
        response = self.client.post("/issue/", json.dumps(self.hard_issue_invalid_user),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def tearDown(self):
        self.user.delete()
        self.leaderboard.delete()
