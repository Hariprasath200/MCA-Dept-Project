# Generated by Django 5.0.1 on 2024-01-10 18:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prasath", "0006_staff1"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Staff",
        ),
        migrations.DeleteModel(
            name="Staff1",
        ),
    ]