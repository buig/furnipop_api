# Generated by Django 4.1.4 on 2023-02-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0025_alter_ida_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemspedidos',
            name='id',
            field=models.IntegerField(db_column='id', primary_key=True, serialize=False),
        ),
    ]
