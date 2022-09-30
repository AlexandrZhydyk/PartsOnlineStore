# Generated by Django 4.1.1 on 2022-09-29 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0006_remove_part_shop_alter_part_part_name"),
        ("cart", "0003_remove_cart_parts"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="quantity",
        ),
        migrations.CreateModel(
            name="CartItem",
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
                ("quantity", models.IntegerField(default=1)),
                (
                    "cart",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="cart.cart"),
                ),
                (
                    "part",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="catalogue.part"),
                ),
            ],
        ),
    ]