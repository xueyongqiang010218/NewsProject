# Generated by Django 2.2 on 2020-12-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_auto_20201231_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstype',
            name='tName',
            field=models.CharField(max_length=50),
        ),
    ]
