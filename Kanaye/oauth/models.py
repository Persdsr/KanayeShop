from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDERS = (
        ('Мужчина', 1),
        ('Женщина', 2)
    )

    surname = models.CharField(verbose_name='Отчество', max_length=15, blank=True, null=True)
    age = models.IntegerField(verbose_name='Возраст')
    gender = models.CharField(verbose_name='Пол', choices=GENDERS)
    phone_number = models.CharField()


