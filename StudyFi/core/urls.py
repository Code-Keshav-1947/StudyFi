from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoogleLoginView, ProfileViewSet, QuestionViewSet, AnswerViewSet, RegisterView, OwnProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"answers", AnswerViewSet)
router.register(r"own-profile", OwnProfileViewSet, basename="own-profile")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("auth/google/", GoogleLoginView.as_view(), name="google-login"),
    path("", include(router.urls)),
]
