from django.urls import reverse

from baran.templatetags.global_tags import baran_date_format
from baran_account.tests.factories import BaranUserFactory
from config_modules import status
from config_modules.test_config import BaseTestWithUserMixin, BaseTestView
from .factories import EmployeeFactory
from ..models import Employee


class TestEmployeesListView(BaseTestWithUserMixin, BaseTestView):
    user_factory = BaranUserFactory

    def get_url(self):
        return reverse('employees_list')

    def test_get(self):
        response = self.make_get_request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'baran_employee/employees_list.html')


class TestEmployeeCreateView(BaseTestWithUserMixin, BaseTestView):
    user_factory = BaranUserFactory

    def get_url(self):
        return reverse('employee_create')

    def get_success_url(self, employee):
        return reverse('employee_details', args=[employee.pk])

    def test_get(self):
        response = self.make_get_request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response,
                                'baran_employee/employee_create.html')

    def get_post_data(self):
        employee = EmployeeFactory.build()
        return {
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'mobile': employee.mobile,
            'start_date': baran_date_format(employee.start_date),
            'position': employee.position,
            'salary': employee.salary,
            'salary_currency': employee.salary_currency,
            'employee_id': employee.employee_id
        }

    def test_post_valid_data(self):
        data = self.get_post_data()

        self.assertFalse(Employee.objects.exists())
        response = self.make_post_request(data)

        self.assertEqual(Employee.objects.count(), 1)
        employee = Employee.objects.first()
        self.assertRedirects(response, self.get_success_url(employee))
        self.assertEqual(employee.first_name, data.get('first_name'))
        self.assertEqual(employee.last_name, data.get('last_name'))
        self.assertEqual(employee.mobile, data.get('mobile'))
        self.assertEqual(baran_date_format(employee.start_date),
                         data.get('start_date'))
        self.assertEqual(employee.position, data.get('position'))
        self.assertEqual(employee.salary, data.get('salary'))
        self.assertEqual(employee.salary_currency, data.get('salary_currency'))
        self.assertEqual(employee.employee_id, data.get('employee_id'))

    def test_post_no_data(self):
        data = {}

        response = self.make_post_request(data)

        self.assertFalse(Employee.objects.exists())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response,
                                'baran_employee/employee_create.html')


class TestEmployeeDetailView(BaseTestWithUserMixin, BaseTestView):
    user_factory = BaranUserFactory

    def setUp(self):
        super().setUp()
        self.employee = EmployeeFactory()

    def get_url(self):
        return reverse('employee_details', args=[self.employee.pk])

    def test_get(self):
        response = self.make_get_request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response,
                                'baran_employee/employee_detail.html')


class TestEmployeeEditView(BaseTestWithUserMixin, BaseTestView):
    user_factory = BaranUserFactory

    def setUp(self):
        super().setUp()
        self.employee = EmployeeFactory()

    def get_url(self):
        return reverse('employee_edit', args=[self.employee.pk])

    def get_success_url(self, employee):
        return reverse('employee_details', args=[self.employee.pk])

    def test_get(self):
        response = self.make_get_request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'baran_employee/employee_edit.html')

    def get_post_data(self):
        return {
            'first_name': self.employee.first_name,
            'last_name': self.employee.last_name,
            'mobile': self.employee.mobile,
            'start_date': baran_date_format(self.employee.start_date),
            'position': self.employee.position,
            'salary': self.employee.salary,
            'salary_currency': 'USD',
        }

    def test_post_valid_data(self):
        data = self.get_post_data()

        self.assertEqual(Employee.objects.count(), 1)
        response = self.make_post_request(data)

        self.assertEqual(Employee.objects.count(), 1)
        employee = Employee.objects.first()
        self.assertRedirects(response, self.get_success_url(employee))
        self.assertEqual(employee.first_name, data.get('first_name'))
        self.assertEqual(employee.last_name, data.get('last_name'))
        self.assertEqual(employee.mobile, data.get('mobile'))
        self.assertEqual(baran_date_format(employee.start_date),
                         data.get('start_date'))
        self.assertEqual(employee.position, data.get('position'))
        self.assertEqual(employee.salary, data.get('salary'))
        self.assertEqual(employee.salary_currency, data.get('salary_currency'))

    def test_post_no_data(self):
        data = {}

        response = self.make_post_request(data)

        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response,
                                'baran_employee/employee_edit.html')


class TestEmployeeDeleteView(BaseTestWithUserMixin, BaseTestView):
    user_factory = BaranUserFactory

    def setUp(self):
        super().setUp()
        self.employee = EmployeeFactory()

    def get_url(self):
        return reverse('employee_delete', args=[self.employee.pk])

    def get_success_url(self):
        return reverse('employees_list')

    def test_get(self):
        response = self.make_get_request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response,
                                'baran_employee/employee_delete.html')

    def test_delete(self):
        self.assertEqual(Employee.objects.count(), 1)
        response = self.make_post_request({})

        self.assertFalse(Employee.objects.exists())
        self.assertRedirects(response, self.get_success_url())
