# Generated by Django 5.0.1 on 2024-01-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prasath", "0011_remove_registration_register_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="email",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="registration",
            name="amount",
            field=models.CharField(max_length=10000),
        ),
    ]
