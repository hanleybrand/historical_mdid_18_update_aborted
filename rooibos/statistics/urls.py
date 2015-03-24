from django.conf.urls import patterns, url
from .views import activity_table, EventList

# rooibos.urls
#  (r'^stats/', include('rooibos.statistics.urls', namespace='stats')),

urlpatterns = patterns('',
    url(r'^$',
        activity_table,
        name='full_table'
    ),
    url(r'^events/([\w-]+)/$',
        EventList.as_view()),
)