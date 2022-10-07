# Generated by Django 4.1.1 on 2022-09-28 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0003_remove_cart_parts"),
        ("catalogue", "0002_remove_part_cart_alter_machinemodel_part_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="part",
            name="cart",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="part",
                to="cart.cart",
            ),
        ),
    ]
