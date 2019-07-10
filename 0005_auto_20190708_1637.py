# Generated by Django 2.2.3 on 2019-07-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demanda', '0004_auto_20190708_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='telephone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='produto',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
