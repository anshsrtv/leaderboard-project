from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from profiles.models import Leaderboard

class LeaderboardTestCase(APITestCase):

    def test_success_with_users(self):

        # Creating 2 test user and their corresponding leaderboard.
        self.first_user = User.objects.create_user(
            email='test_user_1@gmail.com',
            username='testuser_1',
            password='test_password_1',
        )

        self.first_leaderboard = Leaderboard.objects.create(
            user=self.first_user,
            points = 100
        )

        self.second_user = User.objects.create_user(
            email='test_user_2@gmail.com',
            username='testuser_2',
            password='test_password_2',
        )

        self.first_leaderboard = Leaderboard.objects.create(
            user=self.second_user,
            points = 200
        )

        response = self.client.get("/leaderboard/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checking the order in leaderboard.
        self.assertGreaterEqual(int(response.data[0]['points']), int(response.data[1]['points']))

    # def test_fail_without_users(self):
    #     response = self.client.get("/leaderboard/")
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)