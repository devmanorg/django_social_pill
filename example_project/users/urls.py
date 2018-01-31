from functools import partial

from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views


app_name = 'users'

urlpatterns = [
    url(r'^login/$', views.CustomSocialLoginView.as_view(), name='login'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^logout/$', partial(auth_views.logout, template_name='logout.html'), name='logout'),
]
