import datetime
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver    
from django.apps import apps
from .models import Student
from crum import get_current_user

activity_stream = apps.get_model('activitystream', 'ActivityStream')
current_time = datetime.datetime.now().strftime("%Y-%m-%d")


def model_post_save(sender, **kwargs):
    current_user = get_current_user()
    activity = activity_stream(activity="Student %s has beed added by %s at %s" % (kwargs['instance'], current_user, current_time))
    activity.save()
    print("Saved")

@receiver(post_delete, sender=Student)
def model_post_delete(sender, **kwargs):
    current_user = get_current_user()
    activity = activity_stream(activity="Student %s has beed deleted by %s at %s" % (kwargs['instance'], current_user, current_time))
    activity.save()
    print("Deleted")

@receiver(pre_save, sender=Student)
def model_post_edited(sender, **kwargs):
    if kwargs['instance'].id is None:
        model_post_save(sender, **kwargs)
    else:
        current_user = get_current_user()
        activity = activity_stream(activity="Student %s has beed edited by %s at %s" % (kwargs['instance'], current_user, current_time))
        activity.save()
        print("Edited")
