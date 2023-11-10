
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.base_user import AbstractBaseUser

from .login import login_user
from ..backends import FizUserBackend, UrUserBackend
from ..views.email import send_confirmation_email, send_token_email


def registration(request_in, user_model: AbstractBaseUser,
                 form: forms.ModelForm):
    user_model.is_active = False
    user_model.save()
    email = form['email'].value()
    password = form['password'].value()
    if 'full_name' in form.fields:
        full_name = form['full_name'].value()
        auth_user = login_user(request_in, email=email,password=password, full_name=full_name)
    elif 'company_name' in form.fields:
        company_name = form['company_name'].value()
        auth_user = login_user(request_in, email=email, password=password,company_name=company_name)
    send_token_email(auth_user)
    print('send_token_email')
    return auth_user
