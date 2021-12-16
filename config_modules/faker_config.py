import random

from factory import Faker as FactoryBoyFaker
from faker import Faker
from faker.providers import BaseProvider

FAKER_LOCALE = 'en_US'

fake = Faker(FAKER_LOCALE)


class BaranProvider(BaseProvider):
    MIN_SALARY = 1000
    MAX_SALARY = 10000

    def random_salary(self):
        return random.randrange(self.MIN_SALARY, self.MAX_SALARY + 1)


class BaranFactoryBoyFaker(FactoryBoyFaker):
    def __call__(self, **kwargs):
        """Makes the instance of the class callable"""
        self._defaults.update(kwargs)
        return self


class FactoryBoyFakerFactory:
    def __init__(self, locale: str, provider: BaseProvider):
        self._locale = locale
        self._factory = BaranFactoryBoyFaker
        self._factory.add_provider(provider, None)

    def __getattr__(self, item):
        return self._factory(item, locale=self._locale)


fake_boy = FactoryBoyFakerFactory(FAKER_LOCALE, BaranProvider)
