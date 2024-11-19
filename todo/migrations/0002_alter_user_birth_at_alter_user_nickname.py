# Generated by Django 5.1.2 on 2024-11-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]