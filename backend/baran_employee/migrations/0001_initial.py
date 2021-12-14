# Generated by Django 2.2.25 on 2021-12-14 13:15

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('employee_id', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Employee id')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('mobile', models.CharField(blank=True, max_length=64, null=True, verbose_name='Mobile')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('position', models.PositiveSmallIntegerField(choices=[(1, 'Junior Developer'), (1, 'Senior Developer'), (1, 'Team Lead'), (1, 'Project Manager'), (2, 'CEO')], verbose_name='Position')),
                ('salary', models.PositiveIntegerField(verbose_name='Salary')),
                ('salary_currency', models.CharField(max_length=10, verbose_name='Currency')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
