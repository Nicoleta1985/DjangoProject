# Generated by Django 4.0.3 on 2022-03-06 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_alter_professor_department'),
        ('student', '0005_alter_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='professor.professor'),
            preserve_default=False,
        ),
    ]
