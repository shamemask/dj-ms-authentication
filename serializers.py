from rest_framework import serializers

from authentication.UserModel import FizUser, UrUser


class LoginFormSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        error_messages={
            'required': 'Email is required'
        }
    )
    password = serializers.CharField(
        max_length=20,
        required=True,
        error_messages={
            'required': 'Password is required'
        },
        style={'input_type': 'password'}
    )
    remember_me = serializers.BooleanField(required=False, default=False)

class FizUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizUser
        fields = ['email', 'password', 'password2', 'full_name', 'phone', 'promo_code', 'terms_of_service']

class UrUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrUser
        fields = ['email', 'password', 'password2', 'forma', 'city', 'legal_address', 'company_name', 'inn', 'kpp',
                  'bank', 'bik', 'account_number', 'correspondent_account', 'shop', 'full_name', 'phone', 'terms_of_service']
