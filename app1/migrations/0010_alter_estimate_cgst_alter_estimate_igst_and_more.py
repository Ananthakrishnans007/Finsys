# Generated by Django 4.0.6 on 2022-09-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_estimate_cgst_alter_estimate_igst_and_more'),
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