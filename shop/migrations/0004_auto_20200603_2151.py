# Generated by Django 3.0.6 on 2020-06-03 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='phone',
        ),
    ]