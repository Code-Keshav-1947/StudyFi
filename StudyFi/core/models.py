from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# 1. User Profile (Karma/Points के लिए)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=10)  # Sign-up bonus points


# 2. Question/Doubt
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="questions/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


# 3. Answer
class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Agar profile baad me update ho, toh ye save karega
    if hasattr(instance, "profile"):
        instance.profile.save()
