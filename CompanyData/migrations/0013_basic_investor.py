# Generated by Django 3.1.2 on 2020-11-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyData', '0012_auto_20201112_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic',
            name='Investor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
