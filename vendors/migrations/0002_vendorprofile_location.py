# Generated by Django 4.1.7 on 2024-02-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorprofile',
            name='location',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
