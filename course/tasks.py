from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def sendmail():
    send_mail(f"Your subscription on site.",
              f"Update information about your subscription.",
              settings.EMAIL_HOST_USER,
              ["admin@gmail.com"],
              fail_silently=False)
            
@shared_task
def deactivate_user_month():
    all_users =User.objects.filter(is_active=True)
    for user in all_users:
        if user.last_login <= datetime.now() - timedelta(days=5):
            user.is_active = False
            user.save()
            
