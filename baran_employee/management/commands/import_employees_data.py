import os
import re
from datetime import datetime
from os.path import dirname

import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from ...choices import EmployeePositionChoices
from ...models import Employee

COL_INDEX = 0
COL_FIRST_NAME = 1
COL_LAST_NAME = 2
COL_MOBILE = 3
COL_START_DATE = 4
COL_POSITION = 5
COL_SALARY = 6
COL_EMPLOYEE_ID = 7


class Command(BaseCommand):
    help = "Import xlsx table in database"
    FILE_NAME = 'employee_data.xlsx'
    DRY_RUN = False
    SALARY_PATTERN = '^(?P<currency>\\w{3})\\s(?P<salary>\\d+)$'
    DATE_FORMAT = '%d/%m/%Y'

    def add_arguments(self, parser):
        parser.add_argument('-f',
                            '--file',
                            action='store',
                            type=str,
                            default=self.FILE_NAME,
                            help='Specify file name.')

    def handle(self, *args, **options):
        self.file_name = options.get('file')
        with transaction.atomic():
            self.import_employees()

            if self.DRY_RUN:
                raise CommandError('DRY RUN')

    def import_employees(self):
        file_path = os.path.join(dirname(__file__), 'data', self.file_name)
        df = pd.read_excel(file_path, header=0)

        valid_data = []
        error = False
        for row in df.itertuples(index=True):
            row_data = self.get_valid_data(row)
            if not row_data:
                error = True
                # 2 comes from 1 for header and 1 for counting start of 0 :)
                self.stdout.write(f'Error on line number {row[COL_INDEX] + 2}')
                continue
            valid_data.append(row_data)

        if error:
            self.stdout.write(f'Please correct the above errors from the '
                              f'file {file_path}')
            return

        for data in valid_data:
            Employee.objects.create(**data)

    def get_valid_data(self, row) -> {}:
        employee_id = str(row[COL_EMPLOYEE_ID])
        employee = Employee.objects.filter(employee_id=employee_id).first()
        if employee:
            self.stdout.write(f'Employee with employee_id - {employee_id} '
                              f'already exists.')
            return {}
        first_name = row[COL_FIRST_NAME]
        if not first_name:
            self.stdout.write('First name is missing')
            return {}
        last_name = row[COL_LAST_NAME]
        if not last_name:
            self.stdout.write('Last name is missing')
            return {}
        mobile = row[COL_MOBILE]
        if isinstance(mobile, float):
            mobile = f'{mobile:.0f}'
        start_date = row[COL_START_DATE]
        if not start_date:
            self.stdout.write('Start date is missing')
            return {}
        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, self.DATE_FORMAT)
        position = self._get_position(row[COL_POSITION])
        if not position:
            self.stdout.write('Position is missing')
            return {}

        salary = row[COL_SALARY]
        regex = re.compile(self.SALARY_PATTERN, re.UNICODE)
        match = regex.match(salary)
        if not match:
            self.stdout.write('Salary is missing or incorrect format')
            return {}

        salary_sum = int(match.group('salary'))
        salary_currency = match.group('currency')

        return {
            'employee_id': employee_id,
            'first_name': first_name,
            'last_name': last_name,
            'mobile': mobile,
            'start_date': start_date,
            'position': position,
            'salary': salary_sum,
            'salary_currency': salary_currency
        }

    def _get_position(self, position_title) -> int:
        return dict((v, k) for k, v in EmployeePositionChoices.choices) \
            .get(position_title)
