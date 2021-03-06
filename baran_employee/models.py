from django.db import models
from model_utils.models import TimeStampedModel

from .choices import EmployeePositionChoices


class Employee(TimeStampedModel):
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    employee_id = models.CharField(max_length=255, unique=True,
                                   verbose_name='Employee id')
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    mobile = models.CharField(max_length=64, null=True, blank=True,
                              verbose_name='Mobile')
    start_date = models.DateField(verbose_name='Start date')
    position = models.PositiveSmallIntegerField(
        choices=EmployeePositionChoices.choices,
        verbose_name='Position')
    salary = models.PositiveIntegerField(verbose_name='Salary')
    salary_currency = models.CharField(max_length=10, default='BGN',
                                       verbose_name='Currency')

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_salary(self) -> str:
        return f'{self.salary_currency} {self.salary}'

    def __str__(self):
        return f'{self.get_full_name()} ({self.employee_id})'
