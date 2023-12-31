# Generated by Django 4.2.5 on 2023-12-09 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fastbarterApp', '0024_alter_reviews_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='userFrom',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, оставивший отзыв'),
        ),
    ]
