# Generated by Django 4.1.4 on 2023-01-20 14:23

from django.db import migrations, models
import django.db.models.deletion
import furnipop_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0007_alter_imagen_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='furnipop_api.item'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='src',
            field=models.ImageField(blank=True, null=True, upload_to=furnipop_api.models.upload_to),
        ),
        migrations.DeleteModel(
            name='ImagenesItems',
        ),
    ]
