# Generated by Django 3.2.4 on 2021-07-03 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_alter_car_made_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ['-id']},
        ),
    ]
