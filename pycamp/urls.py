from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^activitystream/', include('activitystream.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^admin/', admin.site.urls),
]
