# Generated by Django 4.1.1 on 2022-09-29 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0005_alter_cartitem_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=1,
                        message="Quantity has to be equal or greater then 1.",
                    )
                ],
            ),
        ),
    ]
