# Generated by Django 3.2 on 2021-04-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbworks', '0003_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='names',
            field=models.CharField(default='Nothing', max_length=10),
        ),
    ]
