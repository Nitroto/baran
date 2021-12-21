from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class EmployeePositionChoices(IntegerChoices):
    JUNIOR_DEVELOPER = 1, _('Junior Developer')
    SENIOR_DEVELOPER = 2, _('Senior Developer')
    TEAM_LEAD = 3, _('Team Lead')
    PROJECT_MANAGER = 4, _('Project Manager')
    CEO = 5, _('CEO')
