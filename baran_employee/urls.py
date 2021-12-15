from django.urls import path

from . import views

urlpatterns = [
    path('employees',
         views.EmployeesListView.as_view(),
         name="employees_list"),
    path(f'employee/<int:pk>/',
         views.EmployeeDetailView.as_view(),
         name="employee_details"),
]
