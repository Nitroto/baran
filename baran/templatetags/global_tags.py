from django import template
from django.utils.encoding import force_str

register = template.Library()


@register.filter
def get_errors_messages(errors):
    errors = [force_str(error) for error in errors]
    messages = '\n'.join(errors)
    return messages
