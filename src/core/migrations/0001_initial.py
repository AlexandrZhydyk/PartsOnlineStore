# Generated by Django 4.1.1 on 2022-11-14 16:41

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalogue", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shop",
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
                ("address", models.CharField(max_length=255)),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(
                        max_length=63, null=True
                    ),
                ),
                (
                    "part",
                    models.ManyToManyField(
                        null=True, related_name="shop", to="catalogue.part"
                    ),
                ),
            ],
        ),
    ]
