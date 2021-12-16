from django.test import TestCase

from config_modules.faker_config import fake
from .factories import BaranUserFactory
from ..models import BaranUser


class TestBaranUser(TestCase):
    def setUp(self):
        self.user = BaranUserFactory()

    def test_factory(self):
        self.assertIsNotNone(self.user)
        self.assertIsInstance(self.user, BaranUser)


class TestBaranUserManager(TestCase):
    def test_create_user(self):
        username = fake.user_name()
        password = fake.password()
        user = BaranUser.objects.create_user(username=username,
                                             password=password)

        self.assertIsInstance(user, BaranUser)
        self.assertEqual(user.username, username)
        self.assertFalse(user.is_active)

    def test_create_superuser(self):
        username = fake.user_name()
        password = fake.password()
        user = BaranUser.objects.create_superuser(username=username,
                                                  password=password)

        self.assertIsInstance(user, BaranUser)
        self.assertEqual(user.username, username)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
