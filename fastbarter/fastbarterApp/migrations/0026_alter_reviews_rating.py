# Generated by Django 4.2.5 on 2023-12-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastbarterApp', '0025_remove_reviews_userfrom_alter_reviews_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(default='', max_length=255, verbose_name='Рейтинг'),
        ),
    ]