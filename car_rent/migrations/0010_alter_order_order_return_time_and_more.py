# Generated by Django 4.1.3 on 2022-12-19 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0009_remove_order_order_time_order_order_return_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_return_time',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_station',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_rent.station'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_use_time',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
