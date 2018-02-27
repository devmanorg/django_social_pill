from django.conf import settings

from social_core.backends.base import BaseAuth
from social_core.utils import handle_http_errors

from .telegram_utils import verify_telegram_authentication


class TelegramAuth(BaseAuth):
    """Telegram messenger authentication backend"""
    name = 'telegram'
    ID_KEY = 'id'
    EXTRA_DATA = [
        ('username', 'username'),
        ('first_name', 'first_name'),
        ('last_name', 'last_name'),
        ('photo_url', 'photo_url'),
    ]

    def get_user_details(self, response):
        first_name = response.get('first_name')
        last_name = response.get('last_name')
        return {
            'username': response.get('username'),
            'fullname': '{} {}'.format(first_name, last_name),
            'first_name': first_name,
            'last_name': last_name
        }

    def turn_querydict_into_dict(self, query_dict):
        dict_with_lists = dict(query_dict)
        result = {}
        for key, item in dict_with_lists.items():
            if isinstance(item, list) and len(item) == 1:
                result[key] = item[0]
            else:
                result[key] = item
        return result

    def process_error(self, data):
        bot_token = settings.SOCIAL_PILL_TELEGRAM_BOT_TOKEN
        verify_telegram_authentication(bot_token, request_data=data)

    @handle_http_errors
    def auth_complete(self, request, *args, **kwargs):
        response = self.turn_querydict_into_dict(request.GET.dict())
        self.process_error(data=response)
        kwargs.update({'backend': self, 'response': response})
        return self.strategy.authenticate(*args, **kwargs)

    # This is a different kind of backend: it neither uses redirect
    # nor returns a login page.
    # Instead, there's a JS widget that does all of the work for it.
    def uses_redirect(self):
        return False

    def auth_url(self):
        raise NotImplementedError()

    def auth_html(self):
        raise NotImplementedError()
