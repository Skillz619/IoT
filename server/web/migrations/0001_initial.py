# Generated by Django 3.0.4 on 2020-04-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=200)),
                ('truck', models.CharField(max_length=15)),
                ('employee_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('dustbins', models.TextField()),
                ('employee_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('battery', models.IntegerField()),
                ('number', models.IntegerField()),
                ('ip', models.GenericIPAddressField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]