from django.contrib.auth.hashers import make_password
from django.urls import reverse

from config_modules import status
from config_modules.faker_config import fake
from config_modules.test_config import BaseTestView, BaseTestWithUserMixin
from .factories import BaranUserFactory


class TestIndexView(BaseTestView):
    def get_url(self):
        return reverse('index')

    def test_get_not_logged_user(self):
        response = self.make_get_request()

        self.assertRedirects(response, reverse('login'))

    def test_get_logged_user(self):
        self.user = BaranUserFactory()
        self.client.force_login(self.user)

        response = self.make_get_request()

        self.assertRedirects(response, reverse('employees_list'))


class TestLoginView(BaseTestView):
    def get_url(self):
        return reverse('login')

    def test_get(self):
        response = self.make_get_request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'login.html')

    def test_post(self):
        username = fake.user_name()
        password = fake.password()
        BaranUserFactory(username=username, password=make_password(password))
        data = {
            'username': username,
            'password': password
        }
        response = self.client.post(self.get_url(), data)

        self.assertRedirects(response, reverse('index'),
                             target_status_code=status.HTTP_302_FOUND)


class TestLogoutView(BaseTestWithUserMixin, BaseTestView):
    user_factory = BaranUserFactory

    def get_url(self):
        return reverse('logout')

    def test_get(self):
        response = self.make_get_request()

        self.assertRedirects(response, reverse('index'),
                             target_status_code=status.HTTP_302_FOUND)
