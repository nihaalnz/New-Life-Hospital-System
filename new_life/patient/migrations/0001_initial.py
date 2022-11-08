# Generated by Django 4.1.3 on 2022-11-08 05:45

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region="AE"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                (
                    "eid",
                    models.CharField(
                        max_length=18,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Emirates ID must be in format 111-1111-1111111-1",
                                regex="^(\\d{1,3}(-(\\d{1,4}(-(\\d{1,7}(-(\\d{1,1})?)?)?)?)?)?)$",
                            )
                        ],
                    ),
                ),
            ],
        ),
    ]
