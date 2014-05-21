#from django.conf.urls import *
from django.conf.urls import patterns, url, include, handler500, handler404
from django.contrib import admin
from django.conf import settings
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
from django.views.static import serve
from django.views.decorators.cache import cache_control
from django.http import HttpResponseServerError
from django.template import loader, RequestContext
from rooibos.ui.views import main
from rooibos.access.views import login, logout
from rooibos.legacy.views import legacy_viewer


admin.autodiscover()

apps = filter(lambda a: a.startswith('apps.'), settings.INSTALLED_APPS)
apps_showcases = list(s[5:].replace('.', '-') + '-showcase.html' for s in apps)

# Cache static files
serve = cache_control(max_age=365 * 24 * 3600)(serve)


def handler500_with_context(request):
    template = loader.get_template('500.html')
    return HttpResponseServerError(template.render(RequestContext(request)))


handler404 = getattr(settings, 'HANDLER404', handler404)
handler500 = getattr(settings, 'HANDLER500', handler500_with_context)


def raise_exception():
    raise Exception()


urls = [
    # main page needs SSL because of embedded login form, otherwise CSRF fails
    url(r'^$', main, {'HELP': 'frontpage', 'SSL': True}, name='main'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    #url(r'^showcases/', TemplateView.as_view(HELP='showcases', template='showcases.html', extra_context={'applications': apps_showcases}), name='showcases'))
    url(r'^login/$', login, {'HELP': 'logging-in', 'SSL': True}, name='login'),
    url(r'^logout/$', logout, {'HELP': 'logging-out', 'next_page': settings.LOGOUT_URL}, name='logout'),
    #    url(r'^admin/(.*)', admin.site.root, {'SSL': True}, name='admin'),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/', include(admin.site.urls)),

    # Legacy URL for presentation viewer in earlier version
    url(r'^viewers/view/(?P<record>\d+)/.+/$', legacy_viewer),

    (r'^ui/', include('rooibos.ui.urls', namespace='ui')),
    (r'^acl/', include('rooibos.access.urls', namespace='acl')),
    (r'^explore/', include('rooibos.solr.urls', namespace='explore')),
    (r'^media/', include('rooibos.storage.urls', namespace='media')),
    (r'^data/', include('rooibos.data.urls', namespace='data')),
    (r'^legacy/', include('rooibos.legacy.urls', namespace='legacy')),
    (r'^presentation/', include('rooibos.presentation.urls', namespace='presentation')),
    (r'^viewers/', include('rooibos.viewers.urls', namespace='viewers')),
    (r'^workers/', include('rooibos.workers.urls', namespace='workers')),
    (r'^convert/', include('rooibos.converters.urls', namespace='converters')),
    (r'^api/', include('rooibos.api.urls', namespace='api')),
    (r'^profile/', include('rooibos.userprofile.urls', namespace='profile')),
    (r'^federated/', include('rooibos.federatedsearch.urls', namespace='federated')),
    #    (r'^nasa/', include('rooibos.federatedsearch.nasa.urls')),
    (r'^flickr/', include('rooibos.federatedsearch.flickr.urls', namespace='flickr')),
    (r'^artstor/', include('rooibos.federatedsearch.artstor.urls', namespace='artstor')),
    (r'^shared/$', include('rooibos.federatedsearch.shared.urls', namespace='shared')),
    (r'^impersonate/', include('rooibos.contrib.impersonate.urls', namespace='impersonate')),
    (r'^mediaviewer/', include('rooibos.mediaviewer.urls', namespace='mediaviewer')),
    (r'^megazine/', include('rooibos.megazine.urls', namespace='megazine')),
    (r'^pdfviewer/', include('rooibos.pdfviewer.urls', namespace='pdfviewer')),
    (r'^pptexport/', include('rooibos.pptexport.urls', namespace='pptexport')),
    (r'^audiotextsync/', include('rooibos.audiotextsync.urls', namespace='audiotextsync')),

    url(r'^favicon.ico$', serve, {'document_root': settings.STATIC_DIR, 'path': 'images/favicon.ico'}),
    url(r'^robots.txt$', serve, {'document_root': settings.STATIC_DIR, 'path': 'robots.txt'}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_DIR}, name='static'),

    url(r'^exception/$', raise_exception),
]

for app in apps:
    if not '.' in app[5:]:
        urls.append(url(r'^%s/' % app[5:], include('%s.urls' % app)))

urlpatterns = patterns('', *urls)
