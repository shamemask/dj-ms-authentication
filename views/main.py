import os

from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required

from .login import login_user, login_user_email, login_user_id
from ..backends import FizUserBackend, UrUserBackend
from ..forms.FizForm import FizUserRegistrationForm
from ..forms.LoginForm import LoginForm
from ..forms.UrForm import UrUserRegistrationForm
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

from ..UserModel import UrUser, FizUser
from ..views.email import send_confirmation_email
from ..views.register import registration
from ..logging import logger

# @sync_to_async
# @login_required
@csrf_exempt
def auth(request):
    templ_dict = {}
    user_email = request.session.get('user_email')
    user_id = request.session.get('user_id')
    logger.debug(f'user={user_email}, user_id={user_id}')
    if request.method == 'POST' and not user_email and not user_id:
        data = request.POST
        if 'promo_code' not in data and len(data)>2:
            templ_dict['fizform'] = FizUserRegistrationForm()
            templ_dict['urform'] = UrUserRegistrationForm(request.POST)
            if templ_dict['urform'].is_valid():
                user = UrUser.objects.create_ur(
                    email=templ_dict['urform']['email'].value(),
                    password=templ_dict['urform']['password'].value(),
                    forma=templ_dict['urform']['forma'].value(),
                    city=templ_dict['urform']['city'].value(),
                    legal_address=templ_dict['urform']['legal_address'].value(),
                    company_name=templ_dict['urform']['company_name'].value(),
                    inn=templ_dict['urform']['inn'].value(),
                    kpp=templ_dict['urform']['kpp'].value(),
                    bank=templ_dict['urform']['bank'].value(),
                    bik=templ_dict['urform']['bik'].value(),
                    account_number=templ_dict['urform']['account_number'].value(),
                    correspondent_account=templ_dict['urform']['correspondent_account'].value(),
                    full_name=templ_dict['urform']['full_name'].value(),
                    phone=templ_dict['urform']['phone'].value(),
                    terms_of_service=templ_dict['urform']['terms_of_service'].value(),
                )
                auth_user = registration(request, user, templ_dict['urform'])
                if auth_user is not None:
                    templ_dict['user'] = auth_user
                    return templ_dict
            else:
                templ_dict['logform'] = LoginForm()
                return templ_dict

        elif len(data)>2:
            templ_dict['fizform'] = FizUserRegistrationForm(request.POST)
            templ_dict['urform'] = UrUserRegistrationForm()
            if templ_dict['fizform'].is_valid():
                user = FizUser.objects.create_fiz(
                    email=templ_dict['fizform']['email'].value(),
                    password=templ_dict['fizform']['password'].value(),
                    full_name=templ_dict['fizform']['full_name'].value(),
                    phone=templ_dict['fizform']['phone'].value(),
                    promo_code=templ_dict['fizform']['promo_code'].value(),
                    terms_of_service=templ_dict['fizform']['terms_of_service'].value(),
                )
                auth_user = registration(request, user, templ_dict['fizform'])
                if auth_user is not None:
                    templ_dict['user'] = auth_user
                    return templ_dict

            else:
                templ_dict['logform'] = LoginForm()
                return templ_dict
        else:
            templ_dict['logform'] = LoginForm(request.POST)
            email = templ_dict['logform']['email'].value()
            password = templ_dict['logform']['password'].value()
            auth_user = login_user_email(request, email, password)
            if auth_user is not None:
                templ_dict['user'] = auth_user
                return templ_dict

    if user_email and user_id:
        auth_user = login_user_id(request, user_email, user_id)
        if auth_user is not None:
            templ_dict['user'] = auth_user
    templ_dict['logform'] = LoginForm()
    templ_dict['fizform'] = FizUserRegistrationForm()
    templ_dict['urform'] = UrUserRegistrationForm()
    return templ_dict







