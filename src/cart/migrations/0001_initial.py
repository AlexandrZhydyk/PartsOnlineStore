# Generated by Django 4.1.1 on 2022-11-20 10:32

import catalogue.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalogue", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_type",
                    models.IntegerField(
                        choices=[(1, "GooglePay"), (2, "Visa"), (3, "Cash")], default=1
                    ),
                ),
                ("order_id", models.CharField(default="", max_length=100, null=True)),
                ("ordered", models.BooleanField(default=False)),
                (
                    "delivery_service",
                    models.IntegerField(
                        choices=[
                            (1, "Nova Poshta"),
                            (2, "Meest Express"),
                            (3, "Ukrposhta"),
                            (4, "Self-delivery"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                ("contact_name", models.CharField(max_length=100, null=True)),
                ("contact_surname", models.CharField(max_length=100, null=True)),
                ("city", models.CharField(max_length=100, null=True)),
                ("total_amount", models.FloatField(blank=True, default=0, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "part_number",
                    models.CharField(
                        max_length=50,
                        null=True,
                        validators=[catalogue.validators.part_number_validator],
                    ),
                ),
                (
                    "part_name",
                    models.CharField(
                        max_length=125, null=True, verbose_name="Part name"
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0.01,
                                message="Price has to be greater then 0.01.",
                            )
                        ],
                        verbose_name="Price",
                    ),
                ),
                (
                    "discount",
                    models.FloatField(
                        blank=True,
                        default=1,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=0.01),
                            django.core.validators.MaxValueValidator(limit_value=1),
                        ],
                        verbose_name="Discount",
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart_item",
                        to="cart.cart",
                    ),
                ),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="catalogue.part"
                    ),
                ),
            ],
        ),
    ]
