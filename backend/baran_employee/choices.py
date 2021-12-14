class EmployeePositionChoices:
    JUNIOR_DEVELOPER = 1
    SENIOR_DEVELOPER = 2
    TEAM_LEAD = 3
    PROJECT_MANAGER = 4
    CEO = 5

    @classmethod
    def get_choices(cls):
        return (
            (cls.JUNIOR_DEVELOPER, 'Junior Developer'),
            (cls.SENIOR_DEVELOPER, 'Senior Developer'),
            (cls.TEAM_LEAD, 'Team Lead'),
            (cls.PROJECT_MANAGER, 'Project Manager'),
            (cls.CEO, 'CEO'),
        )
