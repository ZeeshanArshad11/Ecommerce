# Generated by Django 2.2.16 on 2020-12-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20201201_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
