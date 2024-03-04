from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .validators import validate_age

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse email est obligatoire.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
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

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

