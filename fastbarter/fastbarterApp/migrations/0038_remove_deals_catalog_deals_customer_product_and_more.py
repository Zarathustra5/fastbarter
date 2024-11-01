# Generated by Django 4.2.16 on 2024-10-13 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastbarterApp', '0037_remove_deals_customer_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='catalog',
        ),
        migrations.AddField(
            model_name='deals',
            name='customer_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_product', to='fastbarterApp.catalog', verbose_name='Товар пользователя, предложившего обмен'),
        ),
        migrations.AddField(
            model_name='deals',
            name='owner_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fastbarterApp.catalog', verbose_name='Товар владельца объявления'),
        ),
    ]
