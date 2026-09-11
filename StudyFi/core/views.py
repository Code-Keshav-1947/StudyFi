from django.contrib.gis import serializers
from rest_framework import viewsets
from .models import Question, Answer, Profile
from .serializers import QuestionSerializer, AnswerSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]  # Isse koi bhi user questions ko access kar sakta hai
    def perform_create(self, serializer):
        profile = self.request.user.profile

        # Check agar points hain ya nahi
        if profile.points < 5:
            raise serializers.ValidationError(
                {"error": "Doubt poochhne ke liye kam se kam 5 points chahiye!"}
            )

        # 5 Points deduct karo aur save karo
        profile.points -= 5
        profile.save()
        serializer.save(user=self.request.user)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by("-created_at")
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        profile = self.request.user.profile
        profile.points += 10
        profile.save()
        serializer.save(user=self.request.user)


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", "")

        if not username or not password:
            return Response(
                {"error": "Username aur password required hai"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already takened by someone else."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Naya User create karna
        user = User.objects.create_user(
            username=username, password=password, email=email
        )

        # User ke liye Token generate karna
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "User successfully registered.",
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
            },
            status=status.HTTP_201_CREATED,
        )
