# Generated by Django 3.2.2 on 2021-05-11 07:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MasterEntry', '0002_auto_20210511_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_District',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MasterEntry.district', verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_name',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')], verbose_name='Place:'),
        ),
    ]
