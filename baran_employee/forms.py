from django import forms
from django.conf import settings

from .models import Employee


class BaseEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'mobile', 'start_date',
                  'position', 'salary', 'salary_currency', 'employee_id']

    lock_fields = list()
    start_date = forms.DateField(label='Start date',
                                 input_formats=settings.DATE_INPUT_FORMATS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.lock_fields:
            self.fields[field_name].disabled = True
            self.fields[field_name].required = False


class CreateEmployeeForm(BaseEmployeeForm):
    pass


class UpdateEmployeeForm(BaseEmployeeForm):
    lock_fields = ['employee_id']

    def clean_employee_id(self):
        return self.instance.employee_id
