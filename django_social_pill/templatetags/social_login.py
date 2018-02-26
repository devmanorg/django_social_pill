from django import template

register = template.Library()


def construct_context(next_url, is_login, is_large):
    context = {
        'next': next_url,
        'is_login': is_login,
        'is_large': is_large
    }
    return context


@register.inclusion_tag('django_social_pill/github_login.html')
def show_github_login(next_url, is_login, is_large):
    return construct_context(next_url, is_login, is_large)


@register.inclusion_tag('django_social_pill/vk_login.html')
def show_vk_login(next_url, is_login, is_large):
    return construct_context(next_url, is_login, is_large)


@register.inclusion_tag('django_social_pill/facebook_login.html')
def show_facebook_login(next_url, is_login, is_large):
    return construct_context(next_url, is_login, is_large)


@register.inclusion_tag('django_social_pill/twitter_login.html')
def show_twitter_login(next_url, is_login, is_large):
    return construct_context(next_url, is_login, is_large)


@register.inclusion_tag('django_social_pill/google_login.html')
def show_google_login(next_url, is_login, is_large):
    return construct_context(next_url, is_login, is_large)
