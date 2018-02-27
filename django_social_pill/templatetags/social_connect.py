from django import template

from django_social_pill import utils

register = template.Library()


def construct_context(login, login_url, next_url):
    context = {
        'login': login,
        'url': login_url,
        'next': next_url,
    }
    return context


@register.inclusion_tag('django_social_pill/github_connect_tag.html')
def show_github_connect(next_url, user):
    return construct_context(
        utils.get_github_login(user),
        utils.get_github_url(user),
        next_url
    )

@register.inclusion_tag('django_social_pill/vk_connect_tag.html')
def show_vk_connect(next_url, user):
    return construct_context(
        utils.get_vk_name(user),
        utils.get_vk_url(user),
        next_url
    )


@register.inclusion_tag('django_social_pill/facebook_connect_tag.html')
def show_facebook_connect(next_url, user):
    return construct_context(
        utils.get_facebook_name(user),
        utils.get_facebook_url(user),
        next_url
    )


@register.inclusion_tag('django_social_pill/twitter_connect_tag.html')
def show_twitter_connect(next_url, user):
    return construct_context(
        utils.get_twitter_login(user),
        utils.get_twitter_url(user),
        next_url
    )


@register.inclusion_tag('django_social_pill/google_connect_tag.html')
def show_google_connect(next_url, user):
    return construct_context(
        utils.get_google_login(user),
        utils.get_google_url(user),
        next_url
    )


@register.inclusion_tag('django_social_pill/telegram_connect_tag.html')
def show_telegram_connect(user, button_size='large', ask_to_send_messages=False,
                          show_user_photo=True, corner_radius=20):
    context = {
        'login': utils.get_telegram_username(user),
        'url': utils.get_telegram_url(user),
        'button_size': button_size,
        'ask_to_send_messages': ask_to_send_messages,
        'show_user_photo': show_user_photo,
        'corner_radius': corner_radius,
    }
    return context
