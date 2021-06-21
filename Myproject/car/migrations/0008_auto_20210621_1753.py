# Generated by Django 3.2.4 on 2021-06-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_alter_car_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='White', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='made_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='car',
            name='type_of_car',
            field=models.CharField(choices=[('ЛГ', 'Легковая'), ('ВЖ', 'Внедорожник'), ('ГР', 'Грузовик')], default=('ЛГ', 'Легковая'), max_length=2),
        ),
    ]
