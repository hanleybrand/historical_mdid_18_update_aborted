from __future__ import absolute_import

from django.conf.urls import *

from .views import manage, create, edit, duplicate, browse, password, record_usage

urlpatterns = patterns('',
    url(r'^manage/$', view=manage, name='presentation-manage'),
    url(r'^create/$', view=create, name='presentation-create'),
    url(r'^edit/(?P<id>\d+)/(?P<name>[-\w]+)/$', view=edit, name='presentation-edit'),
    url(r'^duplicate/(?P<id>\d+)/(?P<name>[-\w]+)/$', view=duplicate, name='presentation-duplicate'),
    url(r'^browse/$', view=browse, name='presentation-browse'),
    url(r'^password/(?P<id>\d+)/(?P<name>[-\w]+)/$', view=password, name='presentation-password'),
    url(r'^record-usage/(?P<id>\d+)/(?P<name>[-\w]+)/$', view=record_usage, name='presentation-record-usage'),
)
