# Generated by Django 4.2.5 on 2023-12-12 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastbarterApp', '0027_reviews_userto'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='catalog2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catalog2', to='fastbarterApp.catalog', verbose_name='Товар 2'),
        ),
    ]
