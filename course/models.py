from django.db import models
from django.db.models import TextChoices

from users.models import NULLABLE, User


# Create your models here
class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='course_images/', verbose_name='картинка', **NULLABLE)
    description = models.CharField(max_length=200, verbose_name='описание')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='автор', related_name='course_author', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='course_images/', verbose_name='картинка', **NULLABLE)
    description = models.CharField(max_length=200, verbose_name='описание')
    link = models.CharField(max_length=50, verbose_name='ссылка')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='автор', related_name='lesson_author', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='курс', related_name='lessons', **NULLABLE)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    class MethodPayment(TextChoices):
        CASH = 'CA', 'Cash'
        CASHLESS = 'CL', 'Cashless'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_data = models.DateField(auto_now_add=True,verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='оплаченный урок', **NULLABLE)
    summ = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=2, choices=MethodPayment.choices, default=MethodPayment.CASH[0],
                                      verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'{self.user}'