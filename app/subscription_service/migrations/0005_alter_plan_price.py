# Generated by Django 5.0.2 on 2024-02-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_service', '0004_subscription_transaction_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.PositiveIntegerField(default=10),
        ),
    ]