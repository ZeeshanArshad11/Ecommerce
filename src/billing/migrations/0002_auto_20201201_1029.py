# Generated by Django 2.2.16 on 2020-12-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
