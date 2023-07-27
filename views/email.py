from django.contrib.auth import get_user_model
from django.core import signing
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

from .login import login_user
from ..backends import FizUserBackend, UrUserBackend
from ..models2.Email import EmailConfirmation

def confirm_email(request):
    FizUser = FizUserBackend()
    UrUser = UrUserBackend()
    token = request.GET.get('token', None)
    message = 'Ваш аккаунт успешно подтвержден'
    try:
        email = signing.loads(token)
        user = FizUser.get_user(email=email)
        user.is_active = True
        user.save()

        # Вы можете перенаправить пользователя на страницу успешного подтверждения

    except (signing.BadSignature, FizUser.DoesNotExist):
        try:
            email = signing.loads(token)
            user = UrUser.get_user(email=email)
            user.is_active = True
            user.save()
            # Вы можете перенаправить пользователя на страницу успешного подтверждения

        except (signing.BadSignature, UrUser.DoesNotExist):
            # Обработка ошибок, если токен недействителен или пользователь не найден
            message = 'Не верный токен, обратитесь в поддержку'
        # Обработка ошибок, если токен недействителен или пользователь не найден
    templ_dict = {}
    templ_dict['message'] = message
    auth_user = login_user(request, templ_dict['fizform'])
    if auth_user is not None:
        templ_dict['user'] = auth_user
        return templ_dict
    return render(request, 'message.html', templ_dict)
def confirm_email2(request):
    key = request.GET.get('key')
    try:
        confirmation = EmailConfirmation.objects.get(key=key)
    except EmailConfirmation.DoesNotExist:
        return render(request, 'confirmation_failed.html')
    user = confirmation.user
    user.email_verified = True
    user.save()
    confirmation.delete()
    return redirect('confirmation_success')


def send_confirmation_email(request, auth_user):
    user = auth_user
    key = get_random_string(length=64)
    confirmation = EmailConfirmation.objects.create(user=user, key=key)
    # Отправка письма с ссылкой подтверждения
    send_mail(
        'Подтверждение электронной почты',
        f'Пройдите по ссылке для подтверждения вашей электронной почты: {request.build_absolute_uri("/confirm-email/")}?key={key}',
        'noreply@example.com',
        [user.email],
        fail_silently=False,
    )
    return render(request, 'confirmation_sent.html')

def send_token_email(user):
    token = signing.dumps(user.email)
    # Создайте ссылку для подтверждения с использованием токена и uid
    confirmation_link = f"https://outletavto.ru/confirm?token={token}"

    # Отправьте email с токеном
    subject = 'Подтверждение email'
    message = render_to_string('activation_email.html', {'user': user, 'activation_url': confirmation_link})
    send_mail(subject, message, 'snab061@bk.ru', [user.email])