# Generated by Django 3.0.8 on 2020-08-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
