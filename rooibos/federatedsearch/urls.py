from django.conf.urls import *

from views import *

urlpatterns = patterns('',
    url(r'^api/sidebar/$', sidebar_api, name='federatedsearch-sidebar-api'),
)