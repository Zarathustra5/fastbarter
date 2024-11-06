from django.db import models
from users.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class Catalog(models.Model):
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, verbose_name='Фото', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Название товара')
    short_desc = models.CharField(max_length=255, verbose_name='Краткое описание')
    #price = models.CharField(max_length=255, verbose_name='Примерная цена')
    price = models.IntegerField(verbose_name='Примерная цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ForeignKey(Category, verbose_name='Категория товара', on_delete=models.CASCADE, blank=True, null=True)
    category_exchange = models.ForeignKey(Category, verbose_name='Категория товара на обмен', on_delete=models.CASCADE, blank=True, null=True,related_name="category_exchange")
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранное')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Каталог товаров'

class Groups(models.Model):
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, verbose_name='Фото', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Название товара')
    short_desc = models.CharField(max_length=255, verbose_name='Краткое описание')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True,related_name="user")

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Список сообществ'


class Favorite(models.Model):
    catalog = models.ForeignKey(Catalog, verbose_name='Товар', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.catalog}'
    
    class Meta:
        verbose_name = 'Избранный товар'
        verbose_name_plural = 'Избранные товары'

class Reviews(models.Model):
    catalog = models.ForeignKey(Catalog, verbose_name='Товар', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь, оставивший отзыв', on_delete=models.CASCADE, blank=True, null=True, related_name="user_from")
    userTo = models.ForeignKey(CustomUser, verbose_name='Пользователь, которому оставили отзыв', on_delete=models.CASCADE, blank=True, null=True, related_name="user_to")
    review = models.CharField(max_length=255, verbose_name='Отзыв', default='')
    rating = models.CharField(max_length=255, verbose_name='Рейтинг', default='')
    file = models.FileField(upload_to='files/', max_length=None, verbose_name='Файл', blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.catalog}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Deals(models.Model):
    user_owner = models.ForeignKey(CustomUser, verbose_name='Пользователь-владелец объявления', on_delete=models.CASCADE, blank=True, null=True)
    user_customer = models.ForeignKey(CustomUser, verbose_name='Пользователь, предложивший обмен', on_delete=models.CASCADE, blank=True, null=True, related_name="user_customer")
    owner_product = models.ForeignKey(Catalog, verbose_name='Товар владельца объявления', on_delete=models.CASCADE, blank=True, null=True)
    customer_product = models.ForeignKey(Catalog, verbose_name='Товар пользователя, предложившего обмен', on_delete=models.CASCADE, blank=True, null=True,related_name="customer_product")
    status = models.BooleanField(default=False, verbose_name='Завершено')

    def __str__(self):
        return f'{self.owner_product}'
    
    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

class Chats(models.Model):
    deal = models.ForeignKey(Deals, verbose_name='Сделка', on_delete=models.CASCADE, blank=True, null=True)
    is_deleted_user_owner = models.BooleanField(default=False, verbose_name='Удален у пользователя-владельца объявления')
    is_deleted_user_customer = models.BooleanField(default=False, verbose_name='Удален у пользователя, предложившего обмен')

    def __str__(self):
        return f'{self.deal}'
    
    class Meta:
        verbose_name = 'Личный чат'
        verbose_name_plural = 'Личные чаты'

class Messages(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Отправитель', on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=255, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    chat = models.ForeignKey(Chats, verbose_name='Чат', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='files/', max_length=None, verbose_name='Файл', blank=True, null=True, default=False)

    def __str__(self):
        return f'{self.text}'
    
    class Meta:
        verbose_name = 'Сообщение личного чата'
        verbose_name_plural = 'Сообщения личных чатов'

class GroupMessages(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Отправитель', on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=255, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    group = models.ForeignKey(Groups, verbose_name='Сообщество', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='files/', max_length=None, verbose_name='Файл', blank=True, null=True, default=False)

    def __str__(self):
        return f'{self.text}'
    
    class Meta:
        verbose_name = 'Сообщение чата собщества'
        verbose_name_plural = 'Сообщения чатов сообществ'

class Participants(models.Model):
    group = models.ForeignKey(Groups, verbose_name='Сообщество', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Участник сообщества'
        verbose_name_plural = 'Список участников сообществ'