from rest_framework import serializers
from .models import Profile, Question, Answer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProfileSerializer(serializers.ModelSerializer):
    # 'user' ID ki jagah poora UserSerializer return karega
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "points"]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'subject', 'text', 'image', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'text', 'image', 'created_at']
