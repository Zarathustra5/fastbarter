from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name='Почтовый адрес', unique=True)
    phone_number = models.CharField(max_length=100, verbose_name="Номер телефона", unique=False)
    status = models.BooleanField(default=False, verbose_name='Подтверждение аккаунта')
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, verbose_name='Фото', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.fullname
