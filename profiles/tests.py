from rest_framework.test import APITestCase
from rest_framework import status
from profiles.models import Leaderboard
from django.contrib.auth.models import User
import json

class PullRequestTestCase(APITestCase):

    pr_merged_valid_payload = {
        'action':'closed',
        'sender':{
            'login':'testuser',
        },
        "pull_request": {
            'merged': True,
        }
    }

    pr_opened_valid_payload = {
        'action':'opened',
        'sender': {
            'login':'testuser'
        },
        "pull_request": {
            'merged': False,
        }
    }
    pr_opened_invalid_user = {
        'action':'opened',
        'sender': {
            'login':'invalid_user'
        },
        "pull_request": {
            'merged': False,
        }
    }

    invalid_payload = {}

    def setUp(self):
        self.user = User.objects.create_user(
            email = 'test_user@gmail.com',
            username = 'testuser',
            password = 'test_password',
        )

        self.leaderboard = Leaderboard.objects.create(
            username = self.user
        )
    
    def test_success_with_valid_pr_opened(self):
        response = self.client.post("/pull_request/", json.dumps(self.pr_opened_valid_payload),
                                content_type="application/json")
        l_board = Leaderboard.objects.get(username=self.user)
        self.assertNotEqual(l_board.pr_opened,0)
        self.assertEqual(l_board.pr_merged,0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_success_with_valid_pr_merged(self):
        response = self.client.post("/pull_request/", json.dumps(self.pr_merged_valid_payload),
                                content_type="application/json")
        l_board = Leaderboard.objects.get(username=self.user)
        self.assertNotEqual(l_board.pr_merged,0)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_fail_invalid_user(self):
        response = self.client.post("/pull_request/", json.dumps(self.pr_opened_invalid_user),
                                content_type="application/json")
        self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)

    def test_fail_invalid_payload(self):
        response = self.client.post("/pull_request/", json.dumps(self.invalid_payload),
                                content_type="application/json")
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
    

    def tearDown(self):
        self.user.delete()
        self.leaderboard.delete()
