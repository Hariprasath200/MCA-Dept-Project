# Generated by Django 5.0.1 on 2024-01-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prasath", "0009_registration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="amount",
            field=models.CharField(max_length=1000),
        ),
    ]