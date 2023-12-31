# Generated by Django 4.1.3 on 2022-12-22 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("car_rent", "0010_alter_order_order_return_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_return_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_station",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="car_rent.station",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[("未付款", "未付款"), ("已付款", "已付款"), ("使用中", "使用中")],
                default="未付款",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_use_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="transaction_station",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
