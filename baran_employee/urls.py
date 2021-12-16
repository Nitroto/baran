from django.urls import path

from . import views

urlpatterns = [
    path('employees/',
         views.EmployeesListView.as_view(),
         name="employees_list"),
    path('employee/',
         views.EmployeeCreateView.as_view(),
         name="employee_create"),
    path('employee/<int:pk>/',
         views.EmployeeDetailView.as_view(),
         name="employee_details"),
    path('employee/edit/<int:pk>/',
         views.EmployeeEditView.as_view(),
         name="employee_edit"),
    path('employee/delete/<int:pk>/',
         views.EmployeeDeleteView.as_view(),
         name="employee_delete"),
]
