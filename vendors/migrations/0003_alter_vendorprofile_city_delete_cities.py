# Generated by Django 5.0.1 on 2024-01-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_alter_halls_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorprofile',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='cities',
        ),
    ]