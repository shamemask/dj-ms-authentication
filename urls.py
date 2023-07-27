from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import register
from .views.activate import activate
from .views.email import send_confirmation_email, confirm_email
from .views.main import auth

urlpatterns = [
    path('', auth, name='index'),
    path('confirm/', confirm_email, name='confirm_email'),

                  # path('<str:image_name>/', views.image_detail, name='image_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)