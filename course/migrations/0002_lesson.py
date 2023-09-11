# Generated by Django 4.2.5 on 2023-09-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('image', models.ImageField(upload_to='course_images/', verbose_name='картинка')),
                ('description', models.CharField(max_length=200, verbose_name='описание')),
                ('link', models.CharField(max_length=50, verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
