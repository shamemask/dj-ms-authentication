from django.contrib.auth.backends import BaseBackend

from .UserModel import FizUser, UrUser


class FizUserBackend(BaseBackend):
    def authenticate(self, email=None, full_name=None, password=None, **kwargs):
        try:
            User = FizUser.objects.get(email=email, full_name=full_name, password=password)
        except FizUser.DoesNotExist:
            return None

        if User.check_password(password):
            return User

        return None
    def authenticate_email(self, email=None, password=None, **kwargs):
        try:
            User = FizUser.objects.get(email=email, password=password)
        except FizUser.DoesNotExist:
            return None

        if User.check_password(password):
            return User

        return None
    def get_user(self, email):
        try:
            return FizUser.objects.get(email=email)
        except FizUser.DoesNotExist:
            return None
class UrUserBackend(BaseBackend):
    def authenticate(self, email=None, company_name=None, password=None, **kwargs):
        try:
            User = UrUser.objects.get(email=email, company_name=company_name, password=password)
        except UrUser.DoesNotExist:
            return None

        if User.check_password(password):
            return User

        return None
    def authenticate_email(self, email=None, password=None, **kwargs):
        try:
            User = UrUser.objects.get(email=email, password=password)
        except UrUser.DoesNotExist:
            return None

        if User.check_password(password):
            return User

        return None
    def get_user(self, email):
        try:
            return UrUser.objects.get(email=email)
        except UrUser.DoesNotExist:
            return None