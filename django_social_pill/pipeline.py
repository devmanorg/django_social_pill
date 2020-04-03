import requests

from django.core.files.base import ContentFile


DEFAULT_SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'django_social_pill.pipeline.save_user_avatar',
    'django_social_pill.pipeline.save_fb_full_name_as_extra_data',
    'django_social_pill.pipeline.save_vk_full_name_as_extra_data',
)


def set_fullname_as_extra_data(backend, details, uid, *args, **kwargs):
    social = kwargs.get('social') or \
             backend.strategy.storage.user.get_social_auth(backend.name, uid)
    if social:
        social.set_extra_data({'fullname': details.get('fullname')})


def save_vk_full_name_as_extra_data(backend, details, uid, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    set_fullname_as_extra_data(backend, details, uid, **kwargs)


def save_fb_full_name_as_extra_data(backend, details, uid, *args, **kwargs):
    if backend.name != 'facebook':
        return
    set_fullname_as_extra_data(backend, details, uid, **kwargs)


def save_user_avatar(backend, user, response, *args, **kwargs):
    if not hasattr(user, 'avatar') or user.avatar:
        return
    url = None
    ext = None
    if backend.name == 'twitter':
        url = response['profile_image_url']
    if backend.name == 'google-oauth2':
        image = response.get('image')
        url = image and image.get('url')
    elif backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        ext = 'jpg'
    elif backend.name == 'vk-oauth2':
        url = response['user_photo']
    elif backend.name == 'telegram' and 'photo_url' in response:
        url = response['photo_url']
    if url:
        ext = ext or url.split('.')[-1]
        filename = 'avatar.%s' % ext
        content = ContentFile(requests.get(url).content)
        user.avatar.save(filename, content)
        user.save()
