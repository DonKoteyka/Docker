# Generated by Django 4.2.5 on 2023-09-28 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name_plural': 'Склад'},
        ),
        migrations.AlterModelOptions(
            name='stockproduct',
            options={'verbose_name_plural': 'Склад-товары'},
        ),
    ]
