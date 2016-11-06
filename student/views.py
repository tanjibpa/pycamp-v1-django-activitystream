from django.http import HttpResponse

def index(request):
    return HttpResponse("current user: %s" % request.user)
