from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, DeleteView

from baran_account.mixins import BaranPermissionMixin
from .forms import UpdateEmployeeForm, CreateEmployeeForm
from .models import Employee


class EmployeesListView(BaranPermissionMixin, ListView):
    model = Employee
    template_name = 'baran_employee/employees_list.html'


class EmployeeCreateView(BaranPermissionMixin, CreateView):
    model = Employee
    template_name = 'baran_employee/employee_create.html'
    form_class = CreateEmployeeForm

    def get_success_url(self):
        return reverse('employee_details', args=[self.object.pk])


class EmployeeDetailView(BaranPermissionMixin, DetailView):
    model = Employee
    template_name = 'baran_employee/employee_detail.html'


class EmployeeEditView(BaranPermissionMixin, UpdateView):
    model = Employee
    template_name = 'baran_employee/employee_edit.html'
    form_class = UpdateEmployeeForm

    def get_success_url(self):
        return reverse('employee_details', args=[self.object.pk])

    def form_invalid(self, form):
        return super().form_invalid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'baran_employee/employee_delete.html'
    success_url = reverse_lazy('employees_list')
