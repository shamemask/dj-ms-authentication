from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_ur(self, email, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()  # Установите непригодный для использования пароль
        user.save(using=self._db)
        return user
    def create_fiz(self, email, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, **extra_fields)


class FizUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    shop_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Здесь предполагается хранение хэшированного пароля
    phone = models.CharField(max_length=20)
    promo_code = models.CharField(max_length=255, blank=True)
    terms_of_service = models.BooleanField()
    is_active = models.BooleanField(default=False, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Необходимые поля для создания суперпользователя

    def __str__(self):
        return self.email


class UrUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    form = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Здесь предполагается хранение хэшированного пароля
    city = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    legal_address = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)
    kpp = models.CharField(max_length=9)
    bank = models.CharField(max_length=255)
    bik = models.CharField(max_length=9)
    account_number = models.CharField(max_length=20)
    correspondent_account = models.CharField(max_length=20)
    terms_of_service = models.BooleanField()
    is_active = models.BooleanField(default=False, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Необходимые поля для создания суперпользователя

    def __str__(self):
        return self.email
