from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, enrollment, password=None, **extra_fields):
        if not enrollment:
            raise ValueError("Enrollment is required")

        user = self.model(enrollment=enrollment, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, enrollment, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(enrollment, password, **extra_fields)

ROLE_CHOICES = [
        ("student", "Student"),
        ("admin", "Admin"),
    ]
# Create your models here.
class User(AbstractUser):
    username = None
    enrollment = models.CharField(
        max_length=40,
        unique=True
    )
    USERNAME_FIELD = "enrollment"
    REQUIRED_FIELDS = []
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student",
    )

    objects = UserManager()
