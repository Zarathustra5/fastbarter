# Generated by Django 4.2.16 on 2024-11-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastbarterApp', '0039_alter_chats_options_alter_messages_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='price',
            field=models.IntegerField(verbose_name='Примерная цена'),
        ),
    ]
