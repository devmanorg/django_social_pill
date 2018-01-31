from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_social_pill.utils import unlink_appropriate_account


class CustomSocialLoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('users:profile')
        return super().get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        unlink_appropriate_account(self.request.user, self.request)
        return redirect(reverse('users:profile'))

