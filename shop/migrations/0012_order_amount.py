# Generated by Django 3.0.6 on 2020-06-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
