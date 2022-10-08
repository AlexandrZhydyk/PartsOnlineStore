# Generated by Django 4.1.1 on 2022-10-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0006_alter_cartitem_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="payment_type",
            field=models.CharField(
                choices=[(1, "GooglePay"), (2, "Visa"), (3, "PayPal")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]