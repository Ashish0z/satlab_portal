# Generated by Django 4.1.5 on 2023-01-28 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryform',
            old_name='VendorDetials',
            new_name='VendorDetails',
        ),
    ]
