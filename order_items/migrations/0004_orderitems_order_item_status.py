# Generated by Django 4.0.4 on 2022-05-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_items', '0003_rename_price_orderitems_price_per_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='order_item_status',
            field=models.BooleanField(default=False),
        ),
    ]
