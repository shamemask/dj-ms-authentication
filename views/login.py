from urllib import request


from django import forms
from django.contrib.auth import login, authenticate

from ..backends import FizUserBackend, UrUserBackend


def login_user(request_in: request, form: forms.ModelForm):
    email = form['email'].value()
    password = form['password'].value()
    try:
        auth_user = UrUserBackend().authenticate(email=email,
                                                 company_name=form['company_name'].value(),
                                                 password=password)
    except Exception:
        try:
            auth_user = FizUserBackend().authenticate(email=email,
                                                  full_name=form['full_name'].value(),
                                                  password=password)
        except Exception:
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
    return auth_user
