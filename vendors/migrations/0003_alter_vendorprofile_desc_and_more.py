# Generated by Django 4.1.7 on 2024-02-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_vendorprofile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorprofile',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='location',
            field=models.TextField(default=None, null=True),
        ),
    ]
