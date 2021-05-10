# Generated by Django 3.2 on 2021-05-10 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcontact',
            name='dial_code',
            field=models.CharField(choices=[('+91', '+91 (India)'), ('+1', '+1 (US)'), ('+49', '+49 (Germany)'), ('+81', '+81 (Japan)'), ('+33', '+33 (France)'), ('+41', '+41 (Switzerland)')], default='+91', max_length=4),
        ),
        migrations.AddField(
            model_name='joincontact',
            name='dial_code',
            field=models.CharField(choices=[('+91', '+91 (India)'), ('+1', '+1 (US)'), ('+49', '+49 (Germany)'), ('+81', '+81 (Japan)'), ('+33', '+33 (France)'), ('+41', '+41 (Switzerland)')], default='+91', max_length=4),
        ),
        migrations.AlterField(
            model_name='jobcontact',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.RegexValidator(message='Only digits are allowed.', regex='^\\d*$')]),
        ),
        migrations.AlterField(
            model_name='joincontact',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.RegexValidator(message='Only digits are allowed.', regex='^\\d*$')]),
        ),
    ]
