# Generated by Django 5.1.1 on 2024-09-06 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantiry',
            new_name='quantity',
        ),
    ]
