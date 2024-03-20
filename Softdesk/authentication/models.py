from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .validators import validate_age
import bcrypt

class UserManager(BaseUserManager):
    def create_user(self,email,username,age,can_be_contacted,can_be_shared,created_time,is_active, password):
        password_hashed =  password.encode('utf-8')
        password_final = bcrypt.hashpw(password_hashed, bcrypt.gensalt())
        user = User(email,username,age,can_be_contacted,can_be_shared,created_time,is_active,password_final)
        user.save(using=self._db)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name='Adresse email')
    username = models.CharField(max_length=150, unique=True, blank=True, null=True, verbose_name='Nom d\'utilisateur')
    age = models.PositiveIntegerField(blank=True, null=True, validators=[validate_age])
    can_be_contacted = models.BooleanField(default=False, verbose_name='Peut être contacté')
    can_data_be_shared = models.BooleanField(default=False, verbose_name='Peut partager les données')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    password = models.CharField(max_length=150, blank=True, null=True, verbose_name='Mot de passe')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def create_user(self):

        self.password = self.password.encode('utf-8')
        self.password = bcrypt.hashpw(self.password, bcrypt.gensalt())
        self.save(using=self._db)
    def check_hashed_password(self, raw_password):
        raw_password = raw_password.encode('utf-8')
        return bcrypt.checkpw(raw_password, self.password.encode('utf-8'))

    def __str__(self):
        return self.email
