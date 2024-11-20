# Generated by Django 5.1.2 on 2024-11-20 02:10

import django.utils.timezone
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(editable=False, max_length=150)),
                ("last_name", models.CharField(editable=False, max_length=150)),
                (
                    "name",
                    models.CharField(
                        blank=True, help_text="이름", max_length=30, null=True
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        blank=True, help_text="닉네임", max_length=30, null=True
                    ),
                ),
                (
                    "profile",
                    models.CharField(
                        blank=True, help_text="프로필", max_length=150, null=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, default="", help_text="이메일", max_length=50
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, help_text="휴대폰번호", max_length=30, null=True
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(blank=True, help_text="생년월일", null=True),
                ),
                (
                    "push_agree",
                    models.BooleanField(default=True, help_text="푸시 수신 동의"),
                ),
                (
                    "email_agree",
                    models.BooleanField(default=True, help_text="이메일 수신 동의"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", users.models.CustomUserManager()),
            ],
        ),
    ]
