from django import forms

from ..UserModel import FizUser


class FizUserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-silver', 'placeholder': 'Email*'}))

    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'input-silver', 'style': 'font-size:10',
                                                                 'placeholder': 'Введите пароль*'}))
    password2 = forms.CharField(max_length=20,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'input-silver', 'style': 'font-size:10',
                                           'placeholder': 'Повтор пароля*'}))
    full_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'input-silver', 'placeholder': 'Контактное лицо (ФИО)*'}))
    phone = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Телефон*'}))
    promo_code = forms.CharField(max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Промокод'}),
                                 required=False)
    terms_of_service = forms.BooleanField(label='Я ознакомился и принимаю условия договора-оферты',
                                          widget=forms.CheckboxInput(
                                              attrs={'class': 'check-with-label', 'for': "offer"}))

    class Meta:
        model = FizUser
        fields = ('email', 'full_name', 'phone', 'promo_code', 'terms_of_service')


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
