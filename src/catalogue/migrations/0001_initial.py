# Generated by Django 4.1.1 on 2022-09-27 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Part",
            fields=[
                (
                    "part_number",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("part_name", models.CharField(max_length=125, null=True)),
                ("price", models.FloatField(verbose_name="Price")),
                (
                    "discount_price",
                    models.FloatField(blank=True, null=True, verbose_name="Discount"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Part adding date"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="profiles_avatars/empty_avatar.png",
                        null=True,
                        upload_to="profiles_avatars/%Y/%m/%d/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Remark"
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.cart"
                    ),
                ),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.shop"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MachineModel",
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
                ("model", models.CharField(max_length=15, verbose_name="Model")),
                (
                    "machine_type",
                    models.CharField(
                        choices=[
                            (1, "Tractor"),
                            (2, "Combine"),
                            (3, "Self-propelled sprayer"),
                            (4, "Self-propelled forage combine"),
                            (5, "Loader"),
                        ],
                        default="Please choose a machine type",
                        max_length=50,
                        verbose_name="Machine type",
                    ),
                ),
                ("part", models.ManyToManyField(to="catalogue.part")),
            ],
        ),
    ]
