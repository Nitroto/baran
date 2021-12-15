from django.views.generic import ListView, DetailView

from .models import Employee


class EmployeesListView(ListView):
    model = Employee
    template_name = 'baran_employee/employees_list.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'baran_employee/employee_detail.html'