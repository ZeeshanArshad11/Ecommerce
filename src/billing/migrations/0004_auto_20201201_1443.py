# Generated by Django 2.2.16 on 2020-12-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20201201_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
