from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import RedirectView, FormView


class IndexView(RedirectView):
    def get_redirect_url(self, **kwargs):
        user = self.request.user

        if user.is_authenticated:
            return reverse('employees_list')

        return reverse('login')


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user

        if user.is_authenticated:
            return redirect('/')

        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('index')


class LogoutView(RedirectView):
    def get_redirect_url(self, **kwargs):
        logout(self.request)
        return '/'
