# Generated by Django 4.0.3 on 2022-03-06 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='description',
        ),
    ]
