from social_core.backends.base import BaseAuth


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

    def auth_complete(self, request, *args, **kwargs):
        response_with_lists = dict(request.GET.dict())
        response = {}
        for key, item in response_with_lists.items():
            if isinstance(item, list) and len(item) == 1:
                response[key] = item[0]
            else:
                response[key] = item
        kwargs.update(
            {
                'backend': self,
                'response': response,
            }
        )
        return self.strategy.authenticate(*args, **kwargs)

    # This is a different kind of backend: it neither uses redirect
    # nor returns a login page.
    # Instead, there's a JS widget that does all of the work for it.
    def uses_redirect(self):
        return False

    def auth_url(self):
        raise NotImplementedError()

    def auth_html(self):
        return NotImplementedError()
