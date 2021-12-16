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
            self[field_name].field.disabled = True


class CreateEmployeeForm(BaseEmployeeForm):
    pass


class UpdateEmployeeForm(BaseEmployeeForm):
    lock_fields = ['employee_id']
