# Generated by Django 5.0.1 on 2024-01-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prasath", "0005_staff"),
    ]

    operations = [
        migrations.CreateModel(
            name="Staff1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="picture/")),
            ],
            options={
                "verbose_name": "Staff1",
                "verbose_name_plural": "Staff1",
            },
        ),
    ]