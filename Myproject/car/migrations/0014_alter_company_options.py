# Generated by Django 3.2.4 on 2021-07-24 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0013_auto_20210719_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['id'], 'verbose_name_plural': 'Companies'},
        ),
    ]
