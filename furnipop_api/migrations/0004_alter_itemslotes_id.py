# Generated by Django 4.1.4 on 2023-01-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0003_alter_itemslotes_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemslotes',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
