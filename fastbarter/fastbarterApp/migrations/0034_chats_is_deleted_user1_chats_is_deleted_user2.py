# Generated by Django 4.2.16 on 2024-10-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastbarterApp', '0033_remove_chats_catalog_remove_chats_catalog2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='is_deleted_user1',
            field=models.BooleanField(default=False, verbose_name='Удален у пользователя 1'),
        ),
        migrations.AddField(
            model_name='chats',
            name='is_deleted_user2',
            field=models.BooleanField(default=False, verbose_name='Удален у пользователя 2'),
        ),
    ]