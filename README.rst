==================
Django Social Pill
==================

Django Social Pill is a package for a rapid bootstrapping of social authorization.

It builds on top of `Python Social Auth application for Django <https://github.com/python-social-auth/social-app-django>`_ and
allows to never think about various aspects of a typical social authorization adoption.

Installation
------------
1. Add "django_social_pill" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_social_pill',
    ]

2. Add auth backends that you wish to support::

    AUTHENTICATION_BACKENDS = [
        'social_core.backends.github.GithubOAuth2',
        'social_core.backends.vk.VKOAuth2',
        'social_core.backends.facebook.FacebookOAuth2',
        'social_core.backends.google.GoogleOAuth2',
        'social_core.backends.twitter.TwitterOAuth',
        'django.contrib.auth.backends.ModelBackend',
    ]
Github, VK, Facebook, Google and Twitter are the only ones that are supported by now.
`ModelBackend` is needed to support traditional authentication.

3. Add your application-specific settings::

    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/profile/'
    SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/profile/'
    SOCIAL_AUTH_LOGIN_ERROR_URL = '/'

4. Add the keys for every authentication backend::

    SOCIAL_AUTH_GITHUB_KEY = ''
    SOCIAL_AUTH_GITHUB_SECRET = ''
    SOCIAL_AUTH_FACEBOOK_KEY = ''
    SOCIAL_AUTH_FACEBOOK_SECRET = ''
    SOCIAL_AUTH_VK_OAUTH2_KEY = ''
    SOCIAL_AUTH_VK_OAUTH2_SECRET = ''
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
    SOCIAL_AUTH_TWITTER_KEY = ''
    SOCIAL_AUTH_TWITTER_SECRET = ''

5. Add the pipeline::

    from django_social_pill import pipeline

    SOCIAL_AUTH_PIPELINE = pipeline.DEFAULT_SOCIAL_AUTH_PIPELINE

6. Add the social auth urls::

    url('', include('social_django.urls', namespace='social')),

Now you are ready to make use of all built-in features that the app offers.

