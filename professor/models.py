from django.db import models


class Professor(models.Model):
    department_choices = (('math', 'Math'), ('english', 'English'), ('science', 'Science'), ('informatics', 'Informatics'))

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    department = models.CharField(max_length=30, choices=department_choices)
    time = models.TimeField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
