from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    GoogleLoginView,
    ProfileViewSet,
    QuestionViewSet,
    AnswerViewSet,
    RegisterView,
    OwnProfileView,
)

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"answers", AnswerViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("auth/google/", GoogleLoginView.as_view(), name="google-login"),
    path(
        "own-profile/", OwnProfileView.as_view(), name="own-profile"
    ),  # <-- Direct path as_view() ke sath
    path("", include(router.urls)),
]
