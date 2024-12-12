from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    screenname = models.CharField(max_length=150, unique=True)
    city = models.CharField(max_length=100, default='Unknown')
    location = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="images/", 
        default="../default_profile_govdhn"
    )
    is_owner = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance, screenname=instance.username)

post_save.connect(create_profile, sender=User)






