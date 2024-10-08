from django.conf import settings
from django.core.mail import send_mail


def send_account_activate_email(email, email_token):
    subject = "Your account needs to be verified for login"
    email_from = settings.EMAIL_HOST_USER
    message = f'To activate your account please click the link http://127.0.0.1:8000/accounts/activate/{email_token}'
    
    send_mail(subject, message, email_from, [email])