# Generated by Django 3.2 on 2021-04-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbworks', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist', models.CharField(max_length=10)),
            ],
        ),
    ]