# Generated by Django 4.0.3 on 2022-03-06 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
