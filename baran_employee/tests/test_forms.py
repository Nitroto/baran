from baran_employee.forms import BaseEmployeeForm, UpdateEmployeeForm
from config_modules.test_config import BaseTestForm
from .factories import EmployeeFactory
from ..models import Employee


class TestBaseEmployeeForm(BaseTestForm):
    form_class = BaseEmployeeForm

    def setUp(self):
        employee = EmployeeFactory.build(salary_currency='USD')
        self.form_data = {
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'mobile': employee.mobile,
            'start_date': employee.start_date,
            'position': employee.position,
            'salary': employee.salary,
            'salary_currency': employee.salary_currency,
            'employee_id': employee.employee_id
        }

    def test_valid_data(self):
        self.assertValidForm()

    def test_only_mandatory_fields(self):
        del self.form_data['mobile']

        self.assertValidForm()

    def test_missing_first_name(self):
        self.assertMissingField('first_name')

    def test_missing_last_name(self):
        self.assertMissingField('last_name')

    def test_missing_start_date(self):
        self.assertMissingField('start_date')

    def test_missing_position(self):
        self.assertMissingField('position')

    def test_missing_salary(self):
        self.assertMissingField('salary')

    def test_missing_salary_currency(self):
        self.assertMissingField('salary_currency')

    def test_save_form(self):
        form = self.get_form()

        self.assertTrue(form.is_valid())

        employee = form.save()

        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.first_name, self.form_data.get('first_name'))
        self.assertEqual(employee.last_name, self.form_data.get('last_name'))
        self.assertEqual(employee.mobile, self.form_data.get('mobile'))
        self.assertEqual(employee.start_date, self.form_data.get('start_date'))
        self.assertEqual(employee.position, self.form_data.get('position'))
        self.assertEqual(employee.salary, self.form_data.get('salary'))
        self.assertEqual(employee.salary_currency,
                         self.form_data.get('salary_currency'))


class TestUpdateEmployeeForm(BaseTestForm):
    form_class = UpdateEmployeeForm

    def setUp(self):
        self.employee = EmployeeFactory()
        self.form_data = {
            'first_name': self.employee.first_name,
            'last_name': self.employee.last_name,
            'mobile': self.employee.mobile,
            'start_date': self.employee.start_date,
            'position': self.employee.position,
            'salary': self.employee.salary,
            'salary_currency': 'USD'
        }

    def get_form_kwargs(self, **kwargs):
        return {'instance': self.employee}

    def test_valid_data(self):
        self.assertValidForm()

    def test_employee_id_can_not_be_edited(self):
        initial_employee_id = self.employee.employee_id
        employee_id = 'S-6666'
        self.form_data['employee_id'] = employee_id

        form = self.get_form()

        self.assertTrue(form.is_valid())

        instance = form.save()
        self.assertNotEqual(instance.employee_id, employee_id)
        self.assertEqual(instance.employee_id, initial_employee_id)

    def test_save(self):
        form = self.get_form()

        self.assertTrue(form.is_valid())

        employee = form.save()
        self.employee.refresh_from_db()

        self.assertEqual(employee, self.employee)
        self.assertEqual(employee.salary_currency,
                         self.form_data.get('salary_currency'))
