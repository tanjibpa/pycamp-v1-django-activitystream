from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=80)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
