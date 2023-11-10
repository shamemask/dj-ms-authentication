from django.contrib.auth.backends import BaseBackend

from .UserModel import FizUser, UrUser


class FizUserBackend(BaseBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            print('authenticate')
            return FizUser.objects.get(email=email, password=password)
        except FizUser.DoesNotExist:
            print('FizUser.DoesNotExist')
            return None
    def authenticate_email(self, email=None, password=None, **kwargs):
        try:
            User = FizUser.objects.get(email=email, password=password)
        except FizUser.DoesNotExist:
            return None

        return User
    def authenticate_id(self, email=None, id=None, **kwargs):
        try:
            return FizUser.objects.get(email=email, pk=id)
        except FizUser.DoesNotExist:
            return None
    def get_user(self, email):
        try:
            return FizUser.objects.get(email=email)
        except FizUser.DoesNotExist:
            return None
class UrUserBackend(BaseBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            return UrUser.objects.get(email=email, password=password)
        except UrUser.DoesNotExist:
            return None
    def authenticate_email(self, email=None, password=None, **kwargs):
        try:
            return UrUser.objects.get(email=email, password=password)
        except UrUser.DoesNotExist:
            return None
    def authenticate_id(self, email=None, id=None, **kwargs):
        try:
            return UrUser.objects.get(email=email, pk=id)
        except UrUser.DoesNotExist:
            return None
    def get_user(self, email):
        try:
            return UrUser.objects.get(email=email)
        except UrUser.DoesNotExist:
            return None