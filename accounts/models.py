from django.contrib.auth.models import User
from django.db import models

from base.mdels import BaseModel

# Create your models here.

# Profile Model
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_tokn = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='Foles\Profile')