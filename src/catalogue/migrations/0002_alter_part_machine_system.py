# Generated by Django 4.1.1 on 2022-11-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="part",
            name="machine_system",
            field=models.IntegerField(
                choices=[
                    (1, "Engine"),
                    (2, "Transmission"),
                    (3, "Hydraulic"),
                    (4, "Steering and brake"),
                    (5, "Electric"),
                    (6, "Electronic"),
                    (7, "Chassis"),
                    (8, "Other"),
                    (9, "Cab"),
                    (10, "AMS"),
                    (11, "Maintenance"),
                    (12, "Axles"),
                ],
                default=1,
                verbose_name="Machine type",
            ),
        ),
    ]
