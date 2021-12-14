from django.contrib import admin
from django.utils.formats import date_format

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'get_start_date',
                    'get_position', 'salary', 'employee_id')
    search_fields = ['first_name', 'last_name', 'mobile', 'start_date',
                     'salary', 'employee_id']
    list_filter = ('position',)

    def get_start_date(self, obj):
        return date_format(obj.start_date)

    def get_position(self, obj):
        return obj.get_position_display()

    get_start_date.short_description = 'start date'
    get_position.short_description = 'position'


admin.site.register(Employee, EmployeeAdmin)
