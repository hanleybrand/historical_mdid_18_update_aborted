from django.conf.urls import *

from views import *

urlpatterns = patterns('',
    url(r'^install/$', install, name='mediaviewer-install'),
)
