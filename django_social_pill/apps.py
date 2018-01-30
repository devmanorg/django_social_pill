from django.apps import AppConfig
from django.conf import settings
from django.core import exceptions


class DjangoSocialPillConfig(AppConfig):
    name = 'django_social_pill'

    backend_providers = {
        'social_core.backends.github.GithubOAuth2': 'GITHUB',
        'social_core.backends.vk.VKOAuth2': 'VK_OAUTH2',
        'social_core.backends.facebook.FacebookOAuth2': 'FACEBOOK',
        'social_core.backends.google.GoogleOAuth2': 'GOOGLE_OAUTH2',
        'social_core.backends.twitter.TwitterOAuth': 'TWITTER',
    }

    @staticmethod
    def has_keys_needed(settings, provider):
        key_name = 'SOCIAL_AUTH_%s_KEY' % provider
        secret_name = 'SOCIAL_AUTH_%s_SECRET' % provider
        return hasattr(settings, key_name) and hasattr(settings, secret_name)

    def ready(self):
        for backend in settings.AUTHENTICATION_BACKENDS:
            provider = self.backend_providers.get(backend)
            if provider and not self.has_keys_needed(settings, provider):
                message = 'The OAuth keys for %s are missing' % backend
                raise exceptions.ImproperlyConfigured(message)
