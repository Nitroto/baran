import datetime

import factory.fuzzy
from factory.django import DjangoModelFactory

from config_modules.faker_config import fake_boy
from ..choices import EmployeePositionChoices
from ..models import Employee

EMPLOYEE_POSITIONS_IDS = [x[0] for x in EmployeePositionChoices.get_choices()]


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = fake_boy.first_name()
    last_name = fake_boy.last_name()
    mobile = fake_boy.phone_number()
    start_date = datetime.date.today()
    position = factory.fuzzy.FuzzyChoice(EMPLOYEE_POSITIONS_IDS)
    salary = fake_boy.random_salary()
    salary_currency = 'BGN'
    employee_id = factory.Sequence(lambda n: f'S-123{n}')
