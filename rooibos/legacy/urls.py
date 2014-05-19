from django.conf.urls import *
from django.views.generic import TemplateView
from django.conf import settings
from views import *
from rooibos.storage.views import retrieve

urlpatterns = patterns('',
    (r'^WebServices/ImageViewer.asmx/GetInfo$', TemplateView.as_view(template_name='imageviewer_getinfo.xml'),
        {'extra_context': {'namespace': settings.WEBSERVICE_NAMESPACE, 'securelogin': settings.SECURE_LOGIN},
         'mimetype': 'text/xml'}),
    (r'^WebServices/ImageViewer.asmx/Login$', imageviewer_login, {}),
    (r'^WebServices/ImageViewer.asmx/GetSlideshow$', imageviewer_getslideshow, {}),
)
