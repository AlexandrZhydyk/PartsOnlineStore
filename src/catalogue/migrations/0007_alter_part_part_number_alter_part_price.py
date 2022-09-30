# Generated by Django 4.1.1 on 2022-09-29 20:36

import django.core.validators
from django.db import migrations, models

import catalogue.validators


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0006_remove_part_shop_alter_part_part_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="part",
            name="part_number",
            field=models.CharField(
                max_length=50,
                primary_key=True,
                serialize=False,
                validators=[catalogue.validators.part_number_validator],
            ),
        ),
        migrations.AlterField(
            model_name="part",
            name="price",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=0.01, message="Price has to be greater then 0.01."
                    )
                ],
                verbose_name="Price",
            ),
        ),
    ]
