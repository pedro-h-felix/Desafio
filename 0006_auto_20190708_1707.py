# Generated by Django 2.2.3 on 2019-07-08 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demanda', '0005_auto_20190708_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='telephone',
            new_name='tel',
        ),
    ]
