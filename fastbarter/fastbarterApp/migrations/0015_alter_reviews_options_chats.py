# Generated by Django 4.2.5 on 2023-12-01 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fastbarterApp', '0014_delete_category_exchange'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fastbarterApp.catalog', verbose_name='Товар')),
                ('user1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь 1')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь 2')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
    ]