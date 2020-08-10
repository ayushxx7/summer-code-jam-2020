# Generated by Django 3.0.8 on 2020-08-09 04:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=100)),
                ('clean_url', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=500)),
                ('language', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]