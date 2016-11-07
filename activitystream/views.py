from django.http import HttpResponse
from django.shortcuts import render
from .models import ActivityStream

def index(request):
    activities = ActivityStream.objects.all()
    return render(request, 'activitystream/index.html', {'activities': activities})
