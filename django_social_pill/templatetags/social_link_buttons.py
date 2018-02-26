from django import template

from django_social_pill import utils

register = template.Library()


@register.inclusion_tag('django_social_pill/github_link_button.html')
def show_github_link_button(user):
    return {'github_url': utils.get_github_url(user)}


@register.inclusion_tag('django_social_pill/vk_link_button.html')
def show_vk_link_button(user):
    return {'vk_url': utils.get_vk_url(user)}


@register.inclusion_tag('django_social_pill/facebook_link_button.html')
def show_facebook_link_button(user):
    return {'facebook_url': utils.get_facebook_url(user)}


@register.inclusion_tag('django_social_pill/twitter_link_button.html')
def show_twitter_link_button(user):
    return {'twitter_url': utils.get_twitter_url(user)}


@register.inclusion_tag('django_social_pill/telegram_link_button.html')
def show_telegram_link_button(user):
    return {'telegram_url': utils.get_telegram_url(user)}
