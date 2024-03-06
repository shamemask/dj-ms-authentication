import os

from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required

from ..backends import FizUserBackend, UrUserBackend
from ..forms.FizForm import FizUserRegistrationForm
from ..forms.LoginForm import LoginForm
from ..forms.UrForm import UrUserRegistrationForm
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

from ..UserModel import UrUser, FizUser
from ..views.email import send_confirmation_email
from ..views.login import login_user_id, login_user_email
from ..views.register import registration
from ..logging import logger

# @sync_to_async
# @login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import UrUserRegistrationSerializer, FizUserRegistrationSerializer, LoginFormSerializer


@csrf_exempt
# @api_view(['POST'])
def auth_api(request):
    templ_dict = {}
    user_email = request.session.get('user_email')
    user_id = request.session.get('user_id')

    if request.method == 'POST' and not user_email and not user_id:
        data = request.POST

        if 'promo_code' not in data and len(data) > 2:
            ur_form_serializer = UrUserRegistrationSerializer(data=data)
            if ur_form_serializer.is_valid():
                user = ur_form_serializer.save()
                auth_user = registration(request, user, ur_form_serializer)
                if auth_user is not None:
                    templ_dict['user'] = auth_user
                    return templ_dict
            else:
                log_form_serializer = LoginFormSerializer()
                return {'logform': log_form_serializer.data}

        elif len(data) > 2:
            fiz_form_serializer = FizUserRegistrationSerializer(data=data)
            if fiz_form_serializer.is_valid():
                user = fiz_form_serializer.save()
                auth_user = registration(request, user, fiz_form_serializer)
                if auth_user is not None:
                    templ_dict['user'] = auth_user
                    return templ_dict
            else:
                log_form_serializer = LoginFormSerializer()
                return {'logform': log_form_serializer.data}
        else:
            log_form_serializer = LoginFormSerializer(data=data)
            if log_form_serializer.is_valid():
                email = log_form_serializer.validated_data['email']
                password = log_form_serializer.validated_data['password']
                remember_me = log_form_serializer.validated_data['remember_me']

                auth_user = login_user_email(request, email, password)
                if auth_user is not None:
                    templ_dict['user'] = auth_user
                    if remember_me:
                        request.session.set_expiry(604800)
                    else:
                        request.session.set_expiry(0)
                    return templ_dict
            else:
                return {'logform': log_form_serializer.data}

    if user_email and user_id:
        auth_user = login_user_id(request, user_email, user_id)
        if auth_user is not None:
            templ_dict['user'] = auth_user

    log_form_serializer = LoginFormSerializer()
    fiz_form_serializer = FizUserRegistrationSerializer()
    ur_form_serializer = UrUserRegistrationSerializer()
    templ_dict['logform'] = log_form_serializer.data
    templ_dict['fizform'] = fiz_form_serializer.data
    templ_dict['urform'] = ur_form_serializer.data
    return templ_dict





