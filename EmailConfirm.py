from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core import signing

def verify_token(token):
    try:
        email = signing.loads(token)
        # Продолжайте с дальнейшей обработкой, используя извлеченный email
    except signing.BadSignature:
        # Обработайте некорректный или недействительный токен
        pass


class EmailTokenGenerator(PasswordResetTokenGenerator):
    def make_token(self, user):
        # Используйте email пользователя для создания токена
        return self._make_token_with_timestamp(user, user.email)


def send_token_email2(user):
    token = signing.dumps(user.email)
    # Создайте ссылку для подтверждения с использованием токена и uid
    confirmation_link = f"https://outletavto.ru/confirm?token={token}"

    # Отправьте email с токеном
    subject = 'Подтверждение email'
    message = render_to_string('activation_email.html', {'user': user, 'activation_url': confirmation_link})
    send_mail(subject, message, 'snab061@bk.ru', [user.email])

