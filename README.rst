==================
Django Social Pill
==================

Django Social Pill offers convenience tools for routine tasks concerning social authentication.

It builds on top of `Python Social Auth application for Django <https://github.com/python-social-auth/social-app-django>`_ package.

The app was tested out on Django `1.10` and `1.11`.

Deploy the example project
--------------------------

1. :code:`git clone https://github.com/devmanorg/django_social_pill`
2. :code:`cd django_social_pill/example_project`
3. :code:`pip install -r requirements.txt`
4. :code:`python manage.py migrate`
5. Provide the following environment variables:
    - SOCIAL_AUTH_VK_OAUTH2_KEY
    - SOCIAL_AUTH_VK_OAUTH2_SECRET
    - SOCIAL_AUTH_TWITTER_KEY
    - SOCIAL_AUTH_TWITTER_SECRET

    They can be obtained be registering corresponding OAuth apps.
6. :code:`python manage.py runserver`

Installation
------------
1. Add "django_social_pill" and "social_django" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'social_django',
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
:code:`ModelBackend` is needed to support traditional authentication.

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

The Features
------------
Association by email
~~~~~~~~~~~~~~~~~~~~
The default pipeline associates users by email: if the new user has the same email as an existing one, the new user logs in as the existing one.

To ensure that we get user email, we should request it explicitly in the settings::

    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
    SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
      'locale': 'ru_RU',
      'fields': 'id, name, email, age_range'
    }
    SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

Avoid social auth exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are times when we want to hide the server error from users and just display an error message using Django's :code:`messaging` framework.
To do that, it's enough to add the middleware to the end of the list::

     MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',

        ...

        'django_social_pill.middleware.SocialAuthErrorMessageMiddleware',
     ]

Now the targeted page just has to show the message to the user.
Save the avatar
~~~~~~~~~~~~~~~
If your user model has :code:`avatar` attribute, the pipeline will fetch the user picture from social network and assign it to the attribute.

Frontend Features
-----------------
The Dependencies
~~~~~~~~~~~~~~~~

Every inclusion tag in the app makes use of `Bootstrap 3 <https://www.bootstrapcdn.com/>`_,
`Bootstrap Social <https://cdnjs.com/libraries/bootstrap-social>`_ and `Font Awesome <https://www.bootstrapcdn.com/fontawesome/>`_.

The login buttons
~~~~~~~~~~~~~~~~~
Easily add the login buttons to your template::

    {% load social_login %}

    {% show_vk_login next_url is_login is_large %}
    {% show_facebook_login next_url is_login is_large %}
    {% show_google_login next_url is_login is_large %}
    {% show_twitter_login next_url is_login is_large %}
    {% show_github_login next_url is_login is_large %}


The social connect buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~
Already authorized user can add and remove connected accounts with these buttons::

    {% load social_connect %}

    {% show_github_connect next_url user %}
    {% show_vk_connect next_url user %}
    {% show_facebook_connect next_url user %}
    {% show_twitter_connect next_url user %}
    {% show_google_connect next_url user %}
    
May not work very well if Facebook doesn't give us the user name, so be sure to request it explicitly::

    SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
      'locale': 'ru_RU',
      'fields': 'id, name'
    }


The social link buttons
~~~~~~~~~~~~~~~~~~~~~~~
The link buttons allow you you show the connected social networks::

    {% load social_link_buttons %}

    {% show_vk_link_button user %}
    {% show_facebook_link_button user %}
    {% show_twitter_link_button user %}
    {% show_github_link_button user %}


