# Generated by Django 3.1.1 on 2020-11-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faircare', '0002_medicationprice_procedure_procedureprice_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationprice',
            name='state',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='procedureprice',
            name='state',
            field=models.CharField(max_length=2),
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
