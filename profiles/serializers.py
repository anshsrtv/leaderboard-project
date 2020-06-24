from rest_framework import serializers
from profiles.models import Leaderboard
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = [
            "user",
            "points",
            "good_first_issue",
            "milestone_achieved",
            "medium_issues_solved",
            "hard_issues_solved",
            "pr_opened",
            "pr_merged"
        ]