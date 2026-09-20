from rest_framework import serializers
from .models import Profile, Question, Answer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'points']
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'subject', 'text', 'image', 'created_at']
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'text', 'image', 'created_at']