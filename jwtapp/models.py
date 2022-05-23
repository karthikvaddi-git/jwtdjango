from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_superuser(self, email, password):
        user = self._create_user( email, password,username=None,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user



