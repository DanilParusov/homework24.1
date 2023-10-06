from django.core.management.base import BaseCommand
from users.models import User
from course.models import Course, Lesson, Payment
from random import randint, choice
from datetime import date

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

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

        users = User.objects.all()
        courses = []
        for i in range(5):
            course = Course.objects.create(
                title=f'Course {i}',
                description=f'Course description {i}',
                owner=choice(users),
            )
            courses.append(course)
            for j in range(3):
                lesson = Lesson.objects.create(
                    title=f'Lesson {j} for Course {i}',
                    description=f'Lesson description {j} for Course {i}',
                    link=f'lesson{j}_course{i}.pdf',
                    owner=choice(users),
                    course=course,
                )
                Payment.objects.create(
                    user=choice(users),
                    payment_data=date.today(),
                    paid_course=course,
                    paid_lesson=lesson,
                    summ=randint(100, 1000),
                    payment_method=Payment.MethodPayment.CASH if j % 2 == 0 else Payment.MethodPayment.CASHLESS,
                )
