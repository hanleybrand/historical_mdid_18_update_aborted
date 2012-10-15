__author__ = 'hanleybrand'
# thank you http://www.doughellmann.com/PyMOTW/json/
# http://www.voidspace.org.uk/python/articles/cookielib.shtml
import os
import json
import requests
import simplejson
import urllib, urllib2, cookielib
import tempfile
from rooibos.presentation.models import Presentation, PresentationItem
from rooibos.data.models import Record, standardfield
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Attempts to import a Presentation from another mdid3 server\nAvailable commands: serverurl \nex: python manage.py presImport http://mdid3.server.edu'
    args = 'command'

    def handle(self, *commands, **options):
        if not commands:
            print self.help
        else:
            for command in commands:
                print('Currently, the url is hardcoded but in the future %s will be used instead' % command)

            # change to your mdid3 server
            mdidBaseURL = 'http://127.0.0.1/'

            mdidAPI = {
                'auth'          : mdidBaseURL + 'api/login/' ,
                'presentations' : mdidBaseURL + 'api/presentations/currentuser/',
                'presentation'  : mdidBaseURL + 'api/presentation/',
            }

            username = raw_input('enter username')
            promptPass = 'enter password for %s (unmasked)>' % username
            password = raw_input(promptPass)



            currUser = username
            creds = {'username': username, 'password': password}
            r = requests.post(mdidAPI['auth'], data=creds)

            if r.status_code == requests.codes.ok:
                rc = r.cookies
                p = requests.get(mdidAPI['presentations'], cookies=rc)
                print p.status_code

                if p.status_code == requests.codes.ok:
                    j = simplejson.loads(p.content)
                    print('========Slideshows for user %s ========================' % currUser)

                    for presentation in j['presentations']:
                        print presentation['id'], presentation['title'], presentation['tags']



                whichShow = raw_input('enter a slide show id>')

                presUrl = mdidAPI['presentation'] + whichShow
                print 'retrieving: ' + presUrl

                theShow = requests.get(presUrl, cookies = rc)

                if theShow.status_code == requests.codes.ok:
                    jp = simplejson.loads(theShow.content)

                    for slides in jp['content']:
                        print slides


            else:
                    print r.text

"""
{"description": "", "title": "Minecraft", "created": "2012-10-15T13:05:15", "modified": "2012-10-15T13:05:24", "content":
    [{"name": "2012-07-15_224259", "title": "2012-07-15_22.42.59", "image": "/media/get/13/2012-07-15_224259/", "metadata":
        [{"value": "2012-07-15_22.42.59", "label": "Identifier"}, {"value": "2012-07-15_22.42.59", "label": "Title"}], "thumbnail": "/media/thumb/13/2012-07-15_224259/", "id": 13}, {"name": "2012-07-15_224319", "title": "2012-07-15_22.43.19", "image": "/media/get/14/2012-07-15_224319/", "metadata": [{"value": "2012-07-15_22.43.19", "label": "Identifier"}, {"value": "2012-07-15_22.43.19", "label": "Title"}], "thumbnail": "/media/thumb/14/2012-07-15_224319/", "id": 14}, {"name": "2012-07-15_224359", "title": "2012-07-15_22.43.59", "image": "/media/get/15/2012-07-15_224359/", "metadata": [{"value": "2012-07-15_22.43.59", "label": "Identifier"}, {"value": "2012-07-15_22.43.59", "label": "Title"}], "thumbnail": "/media/thumb/15/2012-07-15_224359/", "id": 15}, {"name": "2012-07-15_224453", "title": "2012-07-15_22.44.53", "image": "/media/get/16/2012-07-15_224453/", "metadata": [{"value": "2012-07-15_22.44.53", "label": "Identifier"}, {"value": "2012-07-15_22.44.53", "label": "Title"}], "thumbnail": "/media/thumb/16/2012-07-15_224453/", "id": 16}, {"name": "2012-07-15_225202", "title": "2012-07-15_22.52.02", "image": "/media/get/17/2012-07-15_225202/", "metadata": [{"value": "2012-07-15_22.52.02", "label": "Identifier"}, {"value": "2012-07-15_22.52.02", "label": "Title"}], "thumbnail": "/media/thumb/17/2012-07-15_225202/", "id": 17}, {"name": "2012-07-15_225829", "title": "2012-07-15_22.58.29", "image": "/media/get/18/2012-07-15_225829/", "metadata": [{"value": "2012-07-15_22.58.29", "label": "Identifier"}, {"value": "2012-07-15_22.58.29", "label": "Title"}], "thumbnail": "/media/thumb/18/2012-07-15_225829/", "id": 18}], "result": "ok", "hidden": false, "id": 2, "name": "minecraft-3"}
"""

################
#
#                decoder = json.JSONDecoder()
#
#                def get_decoded_and_remainder(input_data):
#                    obj, end = decoder.raw_decode(input_data)
#                    remaining = input_data[end:]
#                    return (obj, end, remaining)
#
#                print 'JSON first:'
#                obj, end, remaining = get_decoded_and_remainder(jsonData)
#                print 'Object              :', obj
#
#
#                slideCount = 0
#
#
#                for item in obj['content']:
#                    print item['title']
#                    print '\t' + item['name'] # + ' - ' +  item['name'] + ' - ' +  item['metadata']['']
#                    print '\t' + str(item['metadata'][0]['value'])
#                    slideCount = slideCount + 1
#
#                print 'total slides: %s' % slideCount
#
#                # get this from e.g. user input
#                old_slides = ['abc001', 'abc002', 'abc003']
#                target_user_id = 1
#                title = "Old presentation title"
#
#                # work happens here
#                dcidfield = standardfield('identifier')
#                presentation = Presentation.objects.create(title=title, owner=target_user_id)
#
#                for order, dcid in enumerate(old_slides):
#                    records = Record.objects.by_fieldvalue(dcidfield, dcid)
#                    if records:
#                        presentation.items.create(order=order, record=records[0])