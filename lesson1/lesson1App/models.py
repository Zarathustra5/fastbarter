from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class News(models.Model):
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, verbose_name='Фото', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    short_desc = models.CharField(max_length=255, verbose_name='Краткое описание')
    content = models.CharField(max_length=255, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'