# Generated by Django 3.0.6 on 2020-06-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200608_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address1',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=400),
        ),
    ]