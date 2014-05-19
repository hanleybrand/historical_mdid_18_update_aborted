from django.conf.urls import *

from views import *

urlpatterns = patterns('',
    url(r'^powerpoint/$', powerpoint, name='converters-powerpoint'),
 )