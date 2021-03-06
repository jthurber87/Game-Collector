# Generated by Django 3.2.7 on 2021-09-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210919_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='photos',
            field=models.CharField(max_length=500, verbose_name='Photo URL'),
        ),
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.CharField(max_length=50, verbose_name='Player count'),
        ),
    ]
