from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .validators import validate_age
import bcrypt
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, age, can_be_contacted, can_data_be_shared, created_time, is_active, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            age=age,
            can_be_contacted=can_be_contacted,
            can_data_be_shared=can_data_be_shared,
            created_time=created_time,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name='Adresse email')
    username = models.CharField(max_length=150, unique=True, blank=True, null=True, verbose_name='Nom d\'utilisateur')
    age = models.PositiveIntegerField(blank=True, null=True, validators=[validate_age])
    can_be_contacted = models.BooleanField(default=False, verbose_name='Peut être contacté')
    can_data_be_shared = models.BooleanField(default=False, verbose_name='Peut partager les données')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    password = models.CharField(max_length=150, blank=True, null=True, verbose_name='Mot de passe')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time', 'is_active']

    def __str__(self):
        return self.email
    def create_user(self):

        self.password = self.password.encode('utf-8')
        self.password = bcrypt.hashpw(self.password, bcrypt.gensalt())
        self.save(using=self._db)
    def check_hashed_password(self, raw_password):
        raw_password = raw_password.encode('utf-8')
        return bcrypt.checkpw(raw_password, self.password.encode('utf-8'))

    def __str__(self):
        return self.email
