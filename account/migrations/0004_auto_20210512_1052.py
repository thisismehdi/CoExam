# Generated by Django 3.1.7 on 2021-05-12 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210423_0433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='Cne',
            new_name='cne',
        ),
    ]
