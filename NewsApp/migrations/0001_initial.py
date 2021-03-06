# Generated by Django 2.2 on 2020-12-31 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tName', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nTitle', models.CharField(max_length=100, null=True)),
                ('nAuthor', models.CharField(max_length=20, null=True)),
                ('nContent', models.CharField(max_length=1000, null=True)),
                ('nPubDateTime', models.DateTimeField(default=True)),
                ('nStatus', models.BooleanField(default=True)),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsApp.NewsType')),
            ],
        ),
    ]
