# Generated by Django 2.2.16 on 2020-11-28 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20201128_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='billing_Profile',
            new_name='billing_profile',
        ),
    ]
