from django import forms
from django.utils.translation import gettext_lazy as _
from ..UserModel import UrUser
from ..backends import UrUserBackend


def validate_unique_email(email):
    if UrUser.objects.filter(email=email).exists():
        raise forms.ValidationError(
            _('Пользователь с это почтой уже существует'),
            code='invalid_domain'
        )


class UrUserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-silver', 'placeholder': 'Email*'}),
                             validators=[validate_unique_email])

    shop_choices = [
        ('', 'Магазины*'),
        ('Магазин 1', 'Магазин 1'),
        ('Магазин 2', 'Магазин 2'),
        # Добавьте другие варианты магазинов здесь
    ]
    city_choices = [
        ('', 'Города*'),
        ('Город 1', 'Город 1'),
        ('Город 2', 'Город 2'),
        # Добавьте другие варианты городов здесь
    ]

    forma_choices = [
        ('', 'Форма*'),
        ('Форма 1', 'Форма 1'),
        ('Форма 2', 'Форма 2'),
        # Добавьте другие варианты Форм здесь
    ]

    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'input-silver', 'style': 'font-size:10',
                                                                 'placeholder': 'Введите пароль*'}))
    password2 = forms.CharField(max_length=20,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'input-silver', 'style': 'font-size:10',
                                           'placeholder': 'Повтор пароля*'}))
    forma = forms.ChoiceField(choices=city_choices, label='Форма', widget=forms.Select(
        attrs={'class': 'input-silver dropped-wrapper', 'placeholder': 'Форма'}))

    city = forms.ChoiceField(choices=forma_choices, label='Города', widget=forms.Select(
        attrs={'class': 'input-silver dropped-wrapper', 'placeholder': 'Город'}))

    legal_address = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'input-silver', 'placeholder': 'Юридический адрес*'}))

    company_name = forms.CharField(max_length=9,
                                   widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Название*'}))
    inn = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'ИНН*'}))
    kpp = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'КПП*'}))
    bank = forms.CharField(max_length=255,
                           widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Банк*'}))
    bik = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'БИК*'}))
    account_number = forms.CharField(max_length=20,
                                     widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Р/с*'}))
    correspondent_account = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'input-silver', 'placeholder': 'К/c*'}))
    shop = forms.ChoiceField(choices=shop_choices, label='Магазин', widget=forms.Select(
        attrs={'class': 'input-silver dropped-wrapper', 'style': 'border-radius: 10px;', 'placeholder': 'Магазин*'}))
    full_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'input-silver', 'placeholder': 'Контактное лицо (ФИО)*'}))
    phone = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Телефон*'}))
    terms_of_service = forms.BooleanField(label='Я ознакомился и принимаю условия договора-оферты',
                                          widget=forms.CheckboxInput(
                                              attrs={'class': 'check-with-label', 'for': "offer"}))

    class Meta:
        model = UrUser
        fields = ('form', 'shop', 'phone', 'full_name', 'password', 'city', 'organization_name', 'legal_address',
                  'inn', 'kpp', 'bank', 'bik', 'account_number', 'correspondent_account', 'terms_of_service')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
