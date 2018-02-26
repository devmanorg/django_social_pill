def unlink_account(user, provider):
    account = user.social_auth.filter(provider=provider).first()
    if account:
        account.delete()


def unlink_appropriate_account(user, request):
    if 'unlink_github_account' in request.POST:
        unlink_account(user, 'github')
    if 'unlink_vk_account' in request.POST:
        unlink_account(user, 'vk-oauth2')
    if 'unlink_facebook_account' in request.POST:
        unlink_account(user, 'facebook')
    if 'unlink_twitter_account' in request.POST:
        unlink_account(user, 'twitter')
    if 'unlink_google_account' in request.POST:
        unlink_account(user, 'google-oauth2')
    if 'unlink_telegram_account' in request.POST:
        unlink_account(user, 'telegram')


def get_google_login(user):
    auth = user.social_auth.filter(provider='google-oauth2').first()
    return auth.uid if auth else None


def get_telegram_username(user):
    social_auth = user.social_auth.filter(provider='telegram').first()
    if social_auth:
        return social_auth.extra_data['username']


def get_fullname_or_id(social_auth):
    if not social_auth:
        return
    fullname = social_auth.extra_data.get('fullname')
    if fullname:
        return fullname
    return social_auth.uid


def get_vk_name(user):
    """Returns full name from the VK or None if there isn't any

    Requires django_social_pill.pipeline.save_vk_full_name_as_extra_data
    to be present in the pipeline, otherwise the result is always None.
    """
    social_auth = user.social_auth.filter(provider='vk-oauth2').first()
    return get_fullname_or_id(social_auth)


def get_facebook_name(user):
    """Returns full name from the Facebook or None if there isn't any

    Requires django_social_pill.pipeline.save_fb_full_name_as_extra_data
    to be present in the pipeline, otherwise the result is always None.
    """
    social_auth = user.social_auth.filter(provider='facebook').first()
    return get_fullname_or_id(social_auth)


def get_twitter_login(user):
    info = user.social_auth.filter(provider='twitter').first()
    if info and 'access_token' in info.extra_data:
        return info.extra_data['access_token'].get('screen_name')


def get_github_login(user):
    info = user.social_auth.filter(provider='github').first()
    return info.extra_data.get('login', None) if info else None


def get_vk_url(user):
    vk_auth = user.social_auth.filter(provider='vk-oauth2').first()
    if vk_auth:
        return 'https://vk.com/id%s' % vk_auth.uid


def get_facebook_url(user):
    fb_auth = user.social_auth.filter(provider='facebook').first()
    if fb_auth:
        return 'https://facebook.com/%s' % fb_auth.uid


def get_twitter_url(user):
    username = get_twitter_login(user)
    if username:
        return 'https://twitter.com/%s' % username


def get_github_url(user):
    github_login = get_github_login(user)
    if github_login:
        return 'https://github.com/%s' % github_login


def get_google_url(user):
    email = get_google_login(user)
    if email:
        return 'mailto:%s' % email


def get_telegram_url(user):
    username = get_telegram_username(user)
    if username:
        return 'https://telegram.me/%s' % username
