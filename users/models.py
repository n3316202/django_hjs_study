from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class CustomUserManager(UserManager):
    """Custom User Manager Definition"""

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)
    

class User(AbstractUser):
    """Custom User Model Definition"""

    #objects = CustomUserManager()
    USERNAME_FIELD = "username" # 로그인 대상 컬럼(이메일로 하고 싶으면 이메일로)
    REQUIRED_FIELDS = []

    username = models.CharField(
        max_length=150,
        unique=True,
    )
    
    first_name = models.CharField( #한국에서는 성 과 이름을 따로 나누지 않게 하기 위해서
        max_length=150,
        editable=False, # 해당 컬럼은 안나오게
    )
    
    last_name = models.CharField(
        max_length=150,
        editable=False,  # 해당 컬럼은 안나오게
    )

    name = models.CharField(max_length=30, blank=True, null=True, help_text="이름")
    nickname = models.CharField(max_length=30, blank=True, null=True, help_text="닉네임")
    profile = models.CharField(max_length=150, blank=True, null=True, help_text="프로필")
    email = models.EmailField(max_length=50, blank=True, default="", help_text="이메일")
    phone_number = models.CharField(
        max_length=30, blank=True, null=True, help_text="휴대폰번호"
    )
    birth_date = models.DateField(blank=True, null=True, help_text="생년월일")
    push_agree = models.BooleanField(default=True, help_text="푸시 수신 동의")
    email_agree = models.BooleanField(default=True, help_text="이메일 수신 동의")

    def __str__(self):
        return self.username
