from django.db import models
from crum import get_current_user


class Student(models.Model):
    name = models.CharField(max_length=80)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
