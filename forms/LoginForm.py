from django import forms

from ..UserModel import FizUser


class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-silver',
                                                            'placeholder': 'Email или Telagram'}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'input-silver passwordInput',
                                                                 'placeholder': 'Пароль'}))
    class Meta:
        model = FizUser
        fields = ('email', 'password')


