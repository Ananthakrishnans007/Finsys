# Generated by Django 4.0.6 on 2022-09-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_estimate_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='CGST',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='IGST',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='SGST',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='TCS',
            field=models.FloatField(),
        ),
    ]