
from allauth.socialaccount.models import SocialAccount
from django import forms
from django.contrib.auth import login, authenticate

from ..backends import FizUserBackend, UrUserBackend


def login_user(request_in, email, password, company_name='', full_name=''):
    try:
        print('login_user')
        if company_name:
            auth_user = UrUserBackend().authenticate(email=email,
                                                 company_name=company_name,
                                                 password=password)
        else:
            auth_user = FizUserBackend().authenticate(email=email,
                                                      full_name=full_name,
                                                      password=password)
    except Exception as a:
        print('Exception '+a)
    if auth_user is not None:
        print('auth_user is not None')
        login(request_in, auth_user, backend='django.contrib.auth.backends.ModelBackend')
        request_in.session['user_id'] = auth_user.id
        request_in.session['user_email'] = auth_user.email
        request_in.session['user_primary_email'] = auth_user.email
        request_in.session.save()
        return auth_user
def login_user_id(request_in, email, id):
    try:
        auth_user = FizUserBackend().authenticate_id(email=email,
                                                  id=id)
    except Exception:
        try:
            auth_user = UrUserBackend().authenticate_id(email=email,
                                                      id=id)
        except Exception:
            pass
    if auth_user is not None:

        login(request_in, auth_user, backend='django.contrib.auth.backends.ModelBackend')
        request_in.session['user_id'] = auth_user.id
        request_in.session['user_email'] = auth_user.email
        request_in.session['user_primary_email'] = auth_user.email
        request_in.session.save()
        return auth_user
def login_user_email(request_in, email, password):

    try:
        auth_user = FizUserBackend().authenticate_email(email=email,
                                                  password=password)
    except Exception:
        try:
            auth_user = UrUserBackend().authenticate_email(email=email,
                                                      password=password)
        except Exception:
            pass
    if auth_user is not None:

        login(request_in, auth_user, backend='django.contrib.auth.backends.ModelBackend')
        request_in.session['user_id'] = auth_user.id
        request_in.session['user_email'] = auth_user.email
        request_in.session['user_primary_email'] = auth_user.email
        request_in.session.save()
        return auth_user