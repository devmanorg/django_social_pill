from django.contrib.auth import REDIRECT_FIELD_NAME

from social_core import exceptions
from social_django.middleware import SocialAuthExceptionMiddleware


class SocialAuthErrorMessageMiddleware(SocialAuthExceptionMiddleware):

    def get_message(self, request, exception):
        message = 'Что-то пошло не так. Попробуй другую соцсеть'
        if isinstance(exception, exceptions.AuthAlreadyAssociated):
            message = 'Этот аккаунт уже привязан к другому пользователю'
        return message

    def get_redirect_uri(self, request, exception):
        return request.backend.strategy.session_get(REDIRECT_FIELD_NAME)
