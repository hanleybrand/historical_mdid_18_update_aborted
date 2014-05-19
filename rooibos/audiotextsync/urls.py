from django.conf.urls import url, patterns
from views import set_marker


urlpatterns = patterns('',
    url(r'^audiotextsync/(?P<id>[\d]+)/(?P<name>[-\w]+)/setmarker/$', set_marker, name='audiotextsync-setmarker'),
)
