# Generated by Django 5.1.3 on 2024-11-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("complete", models.BooleanField(default=False)),
                ("exp", models.PositiveIntegerField(default=0)),
                ("complete_at", models.DateTimeField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
