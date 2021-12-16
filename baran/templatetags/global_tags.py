import six
from django import template
from django.template.defaultfilters import stringfilter
from django.utils import dateparse
from django.utils.encoding import force_str

register = template.Library()


@register.filter
def get_errors_messages(errors):
    errors = [force_str(error) for error in errors]
    messages = '\n'.join(errors)
    return messages


@register.filter(expects_localtime=True, is_safe=False)
def baran_date_format(value, arg=None):
    from django.template.defaultfilters import date

    if isinstance(value, six.string_types):
        if value in ('', None):
            return ''
        try:
            value = dateparse.parse_date(value)
        except ValueError:
            return value

    if arg is not None:
        return date(value, arg)

    arg = 'd/m/Y'
    return date(value, arg)


@register.inclusion_tag('widgets/input_fields.html')
def show_input(field,):
    assert field, f'Field is not set {force_str(field)}'

    attrs = field.field.widget.attrs
    css_class = 'form-control'

    if attrs and 'class' in attrs:
        css_class = ' '.join([css_class, attrs['class']])

    return {
        'field': field,
        'class': css_class,
        'input_type': field.field.widget.__class__.__name__.lower(),
        'type': field.field.widget.input_type,
        'required': field.field.required,
        'disabled': field.field.disabled,
        'readonly': attrs.get('readonly'),
        'checked': attrs.get('checked'),
    }


@register.filter
@stringfilter
def to_string(value):
    return value
