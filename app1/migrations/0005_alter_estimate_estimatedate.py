# Generated by Django 4.0.6 on 2022-09-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_estimate_estimatedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='estimatedate',
            field=models.CharField(max_length=100),
        ),
    ]
