import json

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

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

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Суперпользователь должен иметь is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Суперпользователь должен иметь is_superuser=True.'))

        return self.create_user(email, **extra_fields)


class FizUser(AbstractBaseUser):
    email = models.EmailField(_('Email'), unique=True)
    shop_name = models.CharField(_('Название магазина'), max_length=255)
    full_name = models.CharField(_('Полное имя'), max_length=255)
    password = models.CharField(_('Пароль'), max_length=255)  # Здесь предполагается хранение хэшированного пароля
    phone = models.CharField(_('Телефон'), max_length=20)
    promo_code = models.CharField(_('Промо-код'), max_length=255, blank=True)
    terms_of_service = models.BooleanField(_('Условия обслуживания'))
    is_active = models.BooleanField(_('Активный статус'), default=False, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Необходимые поля для создания суперпользователя

    def __str__(self):
        return self.email

    def to_json(self):
        return json.dumps({
            'email':self.email,
            'shop_name':self.shop_name,
            'full_name':self.full_name,
            'password':self.password,
            'phone':self.phone,
            'promo_code':self.promo_code,
            'terms_of_service':self.terms_of_service,
            'is_active':self.is_active
        })

    class Meta:
        verbose_name = _('Физ.Лицо')
        verbose_name_plural = _('Физ.Лица')

class UrUser(AbstractBaseUser):
    email = models.EmailField(_('Email'), unique=True)
    form = models.CharField(_('Форма'), max_length=255)
    shop_name = models.CharField(_('Название магазина'), max_length=255)
    phone = models.CharField(_('Телефон'), max_length=20)
    full_name = models.CharField(_('Полное имя'), max_length=255)
    password = models.CharField(_('Пароль'), max_length=255)  # Здесь предполагается хранение хэшированного пароля
    city = models.CharField(_('Город'), max_length=255)
    organization_name = models.CharField(_('Название организации'), max_length=255)
    legal_address = models.CharField(_('Юридический адрес'), max_length=255)
    inn = models.CharField(_('ИНН'), max_length=12)
    kpp = models.CharField(_('КПП'), max_length=9)
    bank = models.CharField(_('Банк'), max_length=255)
    bik = models.CharField(_('БИК'), max_length=9)
    account_number = models.CharField(_('Номер счета'), max_length=20)
    correspondent_account = models.CharField(_('Корреспондентский счет'), max_length=20)
    terms_of_service = models.BooleanField(_('Условия обслуживания'))
    is_active = models.BooleanField(_('Активный статус'), default=False, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Необходимые поля для создания суперпользователя

    def __str__(self):
        return self.email
    def to_json(self):
        return json.dumps({
            'email':self.email,
            'form':self.form,
            'phone':self.phone,
            'shop_name':self.shop_name,
            'full_name':self.full_name,
            'password':self.password,
            'city':self.city,
            'organization_name':self.organization_name,
            'legal_address':self.legal_address,
            'inn':self.inn,
            'kpp':self.kpp,
            'bank':self.bank,
            'bik':self.bik,
            'account_number':self.account_number,
            'correspondent_account':self.correspondent_account,
            'terms_of_service':self.terms_of_service,
            'is_active':self.is_active
        })

    class Meta:
        verbose_name = _('Юр.Лицо')
        verbose_name_plural = _('Юр.Лица')