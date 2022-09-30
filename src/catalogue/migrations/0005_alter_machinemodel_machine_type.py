# Generated by Django 4.1.1 on 2022-09-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0004_alter_machinemodel_machine_type_alter_part_cart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machinemodel",
            name="machine_type",
            field=models.IntegerField(
                choices=[
                    (1, "Tractor"),
                    (2, "Combine"),
                    (3, "Self-propelled sprayer"),
                    (4, "Self-propelled forage combine"),
                    (5, "Loader"),
                ],
                default="Please choose a machine type",
                verbose_name="Machine type",
            ),
        ),
    ]