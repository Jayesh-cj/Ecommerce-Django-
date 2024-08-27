import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.mdels import BaseModel
from base.email import send_account_activate_email

# Create your models here.

# Profile Model
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='Foles/Profile')



@receiver(post_save, sender = User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(
                user = instance,
                email_token = email_token
            )
            email = instance.email
            send_account_activate_email(email, email_token)
    except Exception as e:
        print(e)