# Generated by Django 3.2.5 on 2021-07-09 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_alter_carmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Companies'},
        ),
    ]
