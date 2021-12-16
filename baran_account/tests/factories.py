from factory.django import DjangoModelFactory

from config_modules.faker_config import fake_boy
from ..models import BaranUser

DEFAULT_PASSWORD = 'testpassword'


class BaranUserFactory(DjangoModelFactory):
    class Meta:
        model = BaranUser

    username = fake_boy.user_name()
    first_name = fake_boy.first_name()
    last_name = fake_boy.last_name()
    password = DEFAULT_PASSWORD
    is_staff = False
    is_active = True
