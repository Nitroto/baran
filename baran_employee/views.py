from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .forms import UpdateEmployeeForm, CreateEmployeeForm
from .models import Employee


class EmployeesListView(ListView):
    model = Employee
    template_name = 'baran_employee/employees_list.html'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'baran_employee/employee_create.html'
    form_class = CreateEmployeeForm


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'baran_employee/employee_detail.html'


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'baran_employee/employee_edit.html'
    form_class = UpdateEmployeeForm
