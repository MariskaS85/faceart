# Generated by Django 3.1.6 on 2021-03-02 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210212_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='size',
        ),
    ]
