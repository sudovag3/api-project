# Generated by Django 3.1.5 on 2021-01-12 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210112_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountsandcards',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
