from django.core.management.base import BaseCommand
from course.models import Payment, Course, Lesson
from django.utils import timezone
from random import randint, choice
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        for _ in range(1):  # Adjust the number of records as needed
            user = choice(users)
            course = choice(courses)
            lesson = choice(lessons)
            summ = randint(100, 1000)
            method = choice([x[0] for x in Payment.MethodPayment.choices])
            payment_data = timezone.now()

            Payment.objects.create(
                user=user,
                paid_course=course,
                paid_lesson=lesson,
                summ=summ,
                payment_method=method,
                payment_data=payment_data
            )

            user = User.objects.create(
                email='testt@gmail.com',
                first_name='Admin',
                last_name='SkyPro',
                is_staff=True,
                is_superuser=True,
                is_active=True
            )

            user.set_password('8888')
            user.save()
