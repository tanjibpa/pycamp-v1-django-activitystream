import datetime
from django.db.models.signals import post_save, pre_save, post_delete
from django.core.signals import request_started, request_finished
from django.dispatch import receiver
# from django.contrib.auth.models import User
from django.apps import apps
from .models import Student

activity_stream = apps.get_model('activitystream', 'ActivityStream')
current_time = datetime.datetime.now().strftime("%Y-%m-%d")


@receiver(post_save, sender=Student)
def model_post_save(sender, **kwargs):
    print(kwargs)
    activity = activity_stream(activity="Student %s has beed added at %s" % (kwargs['instance'], current_time))
    activity.save()
    print("Saved")

@receiver(post_delete, sender=Student)
def model_post_delete(sender, **kwargs):
    activity = activity_stream(activity="Student %s has beed deleted at %s" % (kwargs['instance'], current_time))
    activity.save()
    print("Deleted")
