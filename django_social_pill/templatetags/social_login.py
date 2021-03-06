import urllib
from django import template
from django.shortcuts import reverse
from django.conf import settings

register = template.Library()


def construct_context(next_url, is_login, is_large, extra_login_params):
    query_params = {'next': next_url}
    if extra_login_params:
        query_params.update(extra_login_params)
    context = {
        'query_string': urllib.parse.urlencode(query_params),
        'is_login': is_login,
        'is_large': is_large
    }
    return context


@register.inclusion_tag('django_social_pill/github_login.html')
def show_github_login(next_url, is_login, is_large, extra_login_params=None):
    return construct_context(next_url, is_login, is_large, extra_login_params)


@register.inclusion_tag('django_social_pill/vk_login.html')
def show_vk_login(next_url, is_login, is_large, extra_login_params=None):
    return construct_context(next_url, is_login, is_large, extra_login_params)


@register.inclusion_tag('django_social_pill/facebook_login.html')
def show_facebook_login(next_url, is_login, is_large, extra_login_params=None):
    return construct_context(next_url, is_login, is_large, extra_login_params)


@register.inclusion_tag('django_social_pill/twitter_login.html')
def show_twitter_login(next_url, is_login, is_large, extra_login_params=None):
    return construct_context(next_url, is_login, is_large, extra_login_params)


@register.inclusion_tag('django_social_pill/google_login.html')
def show_google_login(next_url, is_login, is_large, extra_login_params=None):
    return construct_context(next_url, is_login, is_large, extra_login_params)


@register.inclusion_tag('django_social_pill/telegram_login.html')
def show_telegram_login(button_size='large', ask_to_send_messages=False,
                        show_user_photo=True, corner_radius=20, next='', extra_login_params=None):
    allowed_button_sizes = ('large', 'medium', 'small')
    if button_size not in allowed_button_sizes:
        raise ValueError(
            'button_size can only be one of {}'.format(allowed_button_sizes)
        )
    if not isinstance(corner_radius, int):
        raise ValueError('corner_radius can only be an integer')
    redirect_url = reverse('social:complete', kwargs={'backend': 'telegram'})
    bot_name = settings.SOCIAL_PILL_TELEGRAM_BOT_NAME

    query_params = {'next': next}
    if extra_login_params:
        query_params.update(extra_login_params)

    return {
        'bot_name': bot_name,
        'redirect_url': redirect_url,
        'button_size': button_size,
        'ask_to_send_messages': ask_to_send_messages,
        'show_user_photo': show_user_photo,
        'corner_radius': corner_radius,
        'query_string': urllib.parse.urlencode(query_params),
    }
