# Generated by Django 3.1.1 on 2020-11-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faircare', '0003_auto_20201126_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationprice',
            name='price',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='procedureprice',
            name='procedure_price',
            field=models.FloatField(max_length=200),
        ),
    ]
