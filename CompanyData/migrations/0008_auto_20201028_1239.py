# Generated by Django 3.0.8 on 2020-10-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyData', '0007_crack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='logo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
