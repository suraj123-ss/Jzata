# Generated by Django 3.1.2 on 2020-11-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyData', '0013_basic_investor'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic',
            name='Products',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
