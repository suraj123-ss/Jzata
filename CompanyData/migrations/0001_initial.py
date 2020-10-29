# Generated by Django 3.0.8 on 2020-10-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campany_name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('Industry', models.CharField(max_length=100)),
                ('Headquatars', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('founded', models.PositiveIntegerField()),
                ('specialities', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('incorporation_date', models.CharField(max_length=100)),
                ('register_address', models.CharField(max_length=100)),
                ('Industry_code', models.CharField(max_length=100)),
            ],
        ),
    ]
