# Generated by Django 2.2.16 on 2020-12-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('orders', '0005_auto_20201128_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='Shipping_address', to='addresses.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='billing_address', to='addresses.Address'),
        ),
    ]