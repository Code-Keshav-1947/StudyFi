from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoogleLoginView, ProfileViewSet, QuestionViewSet, AnswerViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"answers", AnswerViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("google-login/", GoogleLoginView.as_view(), name="google-login"),
    path("", include(router.urls)),
]
