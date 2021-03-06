# Generated by Django 3.1.5 on 2021-01-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_accountsandcards_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsandcards',
            name='date_start',
            field=models.DateField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='depreciations',
            name='date_buy',
            field=models.DateField(verbose_name='Дата покупки'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='financialplan',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
