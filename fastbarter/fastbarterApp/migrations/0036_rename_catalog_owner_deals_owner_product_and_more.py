# Generated by Django 4.2.16 on 2024-10-13 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastbarterApp', '0035_remove_chats_is_deleted_user1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deals',
            old_name='catalog_owner',
            new_name='owner_product',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='catalog_customer',
        ),
        migrations.AddField(
            model_name='deals',
            name='customer_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_product', to='fastbarterApp.catalog', verbose_name='Товар пользователя, предложившего обмен'),
        ),
    ]