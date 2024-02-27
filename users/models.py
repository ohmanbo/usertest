from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    display_name = models.CharField(max_length=16)
    premium_account = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, null=True, blank=True)