from django.db import models

# Create your models here
class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='course_images/', verbose_name='картинка')
    description = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='course_images/', verbose_name='картинка')
    description = models.CharField(max_length=200, verbose_name='описание')
    link = models.CharField(max_length=50, verbose_name='ссылка')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


