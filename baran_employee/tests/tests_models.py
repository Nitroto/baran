from django.test import TestCase
from django.utils.encoding import force_str

from .factories import EmployeeFactory
from ..models import Employee


class TestEmployee(TestCase):
    def setUp(self):
        self.employee = EmployeeFactory()

    def test_factory(self):
        self.assertIsNotNone(self.employee)
        self.assertIsInstance(self.employee, Employee)

    def test_get_full_name(self):
        expect = f'{self.employee.first_name} {self.employee.last_name}'
        self.assertEqual(self.employee.get_full_name(), expect)

    def test_get_salary(self):
        expect = f'{self.employee.salary_currency} {self.employee.salary}'
        self.assertEqual(self.employee.get_salary(), expect)

    def test_repr(self):
        expected = f'{self.employee.get_full_name()} ' \
                   f'({self.employee.employee_id})'
        self.assertEqual(force_str(self.employee), expected)
