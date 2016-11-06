from django.db import models


class ActivityStream(models.Model):
    activity = models.CharField(max_length=200)

    def __str__(self):
        return self.activity
