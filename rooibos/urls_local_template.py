from django.conf.urls.defaults import *

### Add site specific URLS
#     Save this file as "urls_local.py"  in the rooibos dir to add or remap the urls on your local system
#     without having to edit rooibos/urls.py (which might be overwritten by a future update)
#

local_urls = [
    # example of a local url, in this case re-mapping the automatic base url of
    # the app rooibos.apps.mdid-assignments (r'^%s/mdid-assignments') to r'^%s/courses'

    # url(r'^courses/' , include('rooibos.apps.mdid-assignments.urls')),
]
