# Generated by Django 4.0.4 on 2022-05-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Manufacturer name:'),
        ),
    ]
