from rest_framework import viewsets
from .models import Question, Answer, Profile
from .serializers import QuestionSerializer, AnswerSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by("-created_at")
    serializer_class = AnswerSerializer


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", "")

        if not username or not password:
            return Response(
                {"error": "Username aur password dono zaroori hain"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Yeh username pehle se exist karta hai"},
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
                "message": "User successfully register ho gaya!",
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
            },
            status=status.HTTP_201_CREATED,
        )
