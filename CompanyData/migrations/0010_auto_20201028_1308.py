# Generated by Django 3.0.8 on 2020-10-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyData', '0009_auto_20201028_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='Headquatars',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='Industry',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='Industry_code',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='company_no',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='domain',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='founded',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='incorporation_date',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='linkedin',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='logo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='register_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='specialities',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic',
            name='website',
            field=models.TextField(null=True),
        ),
    ]
