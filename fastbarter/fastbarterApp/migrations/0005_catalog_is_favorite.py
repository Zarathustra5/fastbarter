# Generated by Django 4.2.5 on 2023-10-31 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastbarterApp', '0004_catalog_delete_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='is_favorite',
            field=models.BooleanField(default=True, verbose_name='Избранное'),
        ),
    ]
