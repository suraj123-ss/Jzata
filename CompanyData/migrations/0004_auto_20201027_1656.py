# Generated by Django 3.0.3 on 2020-10-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyData', '0003_auto_20201027_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='founded',
            field=models.CharField(max_length=50),
        ),
    ]
