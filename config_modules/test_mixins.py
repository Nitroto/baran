from django.test import TestCase


class BaseTestForm(TestCase):
    form_class = None
    form_data = {}

    def assertValidForm(self):
        form = self.get_form()

        self.assertTrue(form.is_valid())

    def assertMissingField(self, field_name):
        del self.form_data[field_name]

        form = self.get_form()

        errors = form[field_name].errors.as_data()
        self.assertFalse(form.is_valid())
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].code, 'required')

    def assertGetField(self, field_name, expected_value=None):
        expected_value = expected_value or self.form_data.get(field_name)
        form = self.get_form()
        method = getattr(form, f'get_{field_name}', None)

        self.assertTrue(form.is_valid())
        self.assertTrue(callable(method))
        self.assertTrue(method(), expected_value)

    def get_form(self):
        kwargs = self.get_form_kwargs()
        return self.form_class(data=self.form_data, **kwargs)

    def get_form_kwargs(self, **kwargs):
        return {}
