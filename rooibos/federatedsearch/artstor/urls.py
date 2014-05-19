from django.conf.urls import *

from views import *

urlpatterns = patterns('',
    url(r'^artstor/$', search, name='artstor-search'),
)
