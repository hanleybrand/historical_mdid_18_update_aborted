__author__ = 'hanleybrand'
# thank you http://www.doughellmann.com/PyMOTW/json/
# http://www.voidspace.org.uk/python/articles/cookielib.shtml
#import os
#import json
import requests
import simplejson
#import urllib, urllib2, cookielib
#import tempfile
from django.contrib.auth.models import User
from rooibos.presentation.models import Presentation, PresentationItem
from rooibos.data.models import Record, standardfield
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Attempts to import a Presentation from another mdid3 server\nAvailable commands: serverurl \nex: python manage.py presImport http://mdid3.server.edu/ '
    args = 'command'

    def handle(self, *commands, **options):

        mdidBaseURL = None

        if not commands:
            print self.help
        else:
            for command in commands:
                # this is the server url entered when the command was typed e.g.:
                # $> python manage.py import_pres https://mdid3.uni.edu/
                mdidBaseURL = command


        def connect(mdidBaseURL):

            mdidAPI = {
                'auth'          : mdidBaseURL + 'api/login/' ,
                'presentations' : mdidBaseURL + 'api/presentations/currentuser/',
                'presentation'  : mdidBaseURL + 'api/presentation/',
            }

            username = raw_input('enter username -> ')
            promptPass = 'enter password for %s (unmasked)-> ' % username
            password = raw_input(promptPass)

            creds = {'username': username, 'password': password}
            r = requests.post(mdidAPI['auth'], data=creds)

            if r.status_code == requests.codes.ok:
                print 'looks ok', r.status_code
                rc = r.cookies
                presentation_select(r,rc, username)
            else:
                print 'Huh, some kind of weird error - let\'s try again...\n'
                try_again()


        def try_again():
            mdidNewUrl = raw_input('enter the server url with a trailing slash (https://mdid3.uni.edu/) -> ')
            connect(mdidNewUrl)


        def presentation_select(r, rc, username):
            p = requests.get(r.mdidAPI['presentations'], cookies = rc)
            print p.status_code

            if p.status_code == requests.codes.ok:
                j = simplejson.loads(p.content)
                print('========Slideshows for user %s ========================' % username)

                for presentation in j['presentations']:
                    print presentation['id'], presentation['title'], presentation['tags']

                slideCount = 0
                whichShow = raw_input('enter a slide show id > ')
                target_user = chooser(raw_input("enter username to own the slideshow being imported. Press Enter for %s > " % username), username)

                presUrl = r.mdidAPI['presentation'] + whichShow

                print 'retrieving: %s for %s' %  (presUrl, target_user)

                theShow = requests.get(presUrl, cookies = rc)

                # build a list of slides to import
                print theShow.content

                if theShow.status_code == requests.codes.ok:
                    presentation_import(simplejson.loads(theShow.content), target_user, r)
                else:
                    print("Whoops, some sort of error... let's try that again... ")


        def presentation_import(jp, target_user, r):
            #       for slides in jp['content']:

            useSlides = []
            slidesCheck = []
            dcidfield = standardfield('identifier')

            # iterate through the slide list being imported (jp['content'])
            # to get the dc.identifier of each slide for mapping to the local server
            # useSlides[] stores these identifiers

            for order, slide in enumerate(jp['content']):
                for subDict in slide['metadata']:
                    if subDict['label'] == 'Identifier':
                        useSlides.append(subDict['value'])

            if len(useSlides) == 0:

                idChoices = {}

                print "Warning - Identifier mismatch - please specify an ID from the list list"

                for order, slide in enumerate(jp['content'][0]['metadata']):
                    idChoices[str(order)] = slide

                for k in range(len(idChoices)):
                    #for k,v in idChoices.iteritems():
                    print '    ' , str(k), '-', idChoices[str(k)].values()

                useID = raw_input('enter the number of the field used as an identifier the local system > ');
                otherID = jp['content'][0]['metadata'][int(useID)]['label']

                print 'using' , otherID , 'as remote Identifier'

                for order, slide in enumerate(jp['content']):
                    for subDict in slide['metadata']:
                        if subDict['label'] == otherID:
                            useSlides.append(subDict['value'])

                print useSlides


            for identifier in useSlides:
                #czechRec = Record.by_fieldvalue(dcidfield, identifier)
                try:
                    czechRec = Record.get_or_404(Record.objects.get(name=identifier), target_user)
                    print  '%s - this record exists: %s' % (identifier, czechRec)
                except Record.DoesNotExist:
                    print identifier, 'does not exist'

#       useSlides.append({ "thumbnail"  : slides['thumbnail'],
#                                           "image"      : slides['image'] ,
#                                           "title"      : slides['title'],
#                                           "name"       : slides['name'],
#                                           "identifier" : czechRec.id} )


    #print title and number of slides
                    print jp['title'], len(jp['content'])
                    print useSlides

                    concat_description = jp['description']


#                    presentation = Presentation.objects.create(title=jp['title'], owner=target_user, description=concat_description)

#                    for order, dcid in enumerate(useSlides):
#                        records = Record.objects.by_fieldvalue(dcidfield, dcid)
#                        if records:
#                            presentation.items.create(order=order, record=records[0])
            else:
                print r.text

        if mdidBaseURL:
            connect(mdidBaseURL)
        else:
            try_again()

def chooser(anotherUser, me, inception = 0):
    # inception is to keep track of recursive calls to chooser
    if anotherUser != '':
        try:
            usr = User.objects.get(username=anotherUser)
        except User.DoesNotExist:
            print 'ALERT: User with username %s not found' % anotherUser
            anotherTry = raw_input('Try another username? (Press Enter for %s) > ' % me)
            usr = chooser(anotherTry, me, inception + 1)
    else:
        try:
            usr = User.objects.get(username=me)
        except User.DoesNotExist:
            print 'ALERT: The account on the remote machine used for login  %s not found on local server' % me
            anotherTry = raw_input('Try another username? (Press Enter for %s) > ' % me)
            usr = chooser(anotherTry, me, inception + 1)
    if inception == 0:
        print 'Returning %s for user %s' % (usr.id, usr.username)
    return usr



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




#
#"""
#{"description": "", "title": "Minecraft", "created": "2012-10-15T13:05:15", "modified": "2012-10-15T13:05:24", "content":
#    [{"name": "2012-07-15_224259", "title": "2012-07-15_22.42.59", "image": "/media/get/13/2012-07-15_224259/", "metadata":
#        [{"value": "2012-07-15_22.42.59", "label": "Identifier"}, {"value": "2012-07-15_22.42.59", "label": "Title"}], "thumbnail": "/media/thumb/13/2012-07-15_224259/", "id": 13}, {"name": "2012-07-15_224319", "title": "2012-07-15_22.43.19", "image": "/media/get/14/2012-07-15_224319/", "metadata": [{"value": "2012-07-15_22.43.19", "label": "Identifier"}, {"value": "2012-07-15_22.43.19", "label": "Title"}], "thumbnail": "/media/thumb/14/2012-07-15_224319/", "id": 14}, {"name": "2012-07-15_224359", "title": "2012-07-15_22.43.59", "image": "/media/get/15/2012-07-15_224359/", "metadata": [{"value": "2012-07-15_22.43.59", "label": "Identifier"}, {"value": "2012-07-15_22.43.59", "label": "Title"}], "thumbnail": "/media/thumb/15/2012-07-15_224359/", "id": 15}, {"name": "2012-07-15_224453", "title": "2012-07-15_22.44.53", "image": "/media/get/16/2012-07-15_224453/", "metadata": [{"value": "2012-07-15_22.44.53", "label": "Identifier"}, {"value": "2012-07-15_22.44.53", "label": "Title"}], "thumbnail": "/media/thumb/16/2012-07-15_224453/", "id": 16}, {"name": "2012-07-15_225202", "title": "2012-07-15_22.52.02", "image": "/media/get/17/2012-07-15_225202/", "metadata": [{"value": "2012-07-15_22.52.02", "label": "Identifier"}, {"value": "2012-07-15_22.52.02", "label": "Title"}], "thumbnail": "/media/thumb/17/2012-07-15_225202/", "id": 17}, {"name": "2012-07-15_225829", "title": "2012-07-15_22.58.29", "image": "/media/get/18/2012-07-15_225829/", "metadata": [{"value": "2012-07-15_22.58.29", "label": "Identifier"}, {"value": "2012-07-15_22.58.29", "label": "Title"}], "thumbnail": "/media/thumb/18/2012-07-15_225829/", "id": 18}], "result": "ok", "hidden": false, "id": 2, "name": "minecraft-3"}
#"""

################
#                lookupShow = urllib2.Request(presUrl)
#                lookUpResult = urllib2.urlopen(lookupShow)
#
#                #print lookUpResult.read()
#
#                t = tempfile.NamedTemporaryFile(mode='w+')
#                json.dump(lookUpResult.read(),t)
#                t.flush()
#                t.seek(0)
#
#                jsonFile = json.load(t)
#
#                #jsonFile = open('slideShow.json')
#                try:
#                    jsonData = jsonFile
#                finally:
#                    t.close()
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


                # if os.path.isfile(COOKIEFILE):
                # if we have a cookie file already saved
                # then load the cookies into the Cookie Jar
                #    cj.load(COOKIEFILE)

                #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                #urllib2.install_opener(opener)

                #logMeIn = urllib2.Request(mdidAPI['auth'], credStr)
                #logInResult = urllib2.urlopen(logMeIn)



                #cj.save(COOKIEFILE)                     # save the cookies again

"""
sample output

session info : {"sessionid": "3dde7565e6fd090479aaa46dfd0e9df7", "userid": 26, "result": "ok"}
retrieving: http://mdid3.temple.edu/api/presentation/4970
JSON first:
Object              : {u'description': None, u'created': u'2011-12-20T18:55:03', u'title': u'futurism bragaglia', u'modified': u'2011-12-20T18:55:03', u'content': [{u'name': u'r-2250176', u'title': u'Trying', u'image': u'/media/get/12420/r-2250176/', u'thumbnail': u'/media/thumb/12420/r-2250176/', u'id': 12420, u'metadata': [{u'value': u'SL-20BRAA001', u'label': u'ID'}, {u'value': u'Trying', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-6635695', u'title': u'ritratto polifisionomico', u'image': u'/media/get/12421/r-6635695/', u'thumbnail': u'/media/thumb/12421/r-6635695/', u'id': 12421, u'metadata': [{u'value': u'SL-20BRAA002', u'label': u'ID'}, {u'value': u'ritratto polifisionomico', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-8183409', u'title': u'Young Man Swinging', u'image': u'/media/get/12422/r-8183409/', u'thumbnail': u'/media/thumb/12422/r-8183409/', u'id': 12422, u'metadata': [{u'value': u'SL-20BRAA003', u'label': u'ID'}, {u'value': u'Young Man Swinging', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-6811396', u'title': u'Ducking', u'image': u'/media/get/12423/r-6811396/', u'thumbnail': u'/media/thumb/12423/r-6811396/', u'id': 12423, u'metadata': [{u'value': u'SL-20BRAA004', u'label': u'ID'}, {u'value': u'Ducking', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-5137792', u'title': u'Greetings', u'image': u'/media/get/12424/r-5137792/', u'thumbnail': u'/media/thumb/12424/r-5137792/', u'id': 12424, u'metadata': [{u'value': u'SL-20BRAA005', u'label': u'ID'}, {u'value': u'Greetings', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-1403707', u'title': u'dattilografa', u'image': u'/media/get/12425/r-1403707/', u'thumbnail': u'/media/thumb/12425/r-1403707/', u'id': 12425, u'metadata': [{u'value': u'SL-20BRAA006', u'label': u'ID'}, {u'value': u'dattilografa', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-7633456', u'title': u'Going Around', u'image': u'/media/get/12426/r-7633456/', u'thumbnail': u'/media/thumb/12426/r-7633456/', u'id': 12426, u'metadata': [{u'value': u'SL-20BRAA007', u'label': u'ID'}, {u'value': u'Going Around', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-7680059', u'title': u'Futurist Painter Giacomo Balla', u'image': u'/media/get/12427/r-7680059/', u'thumbnail': u'/media/thumb/12427/r-7680059/', u'id': 12427, u'metadata': [{u'value': u'SL-20BRAA008', u'label': u'ID'}, {u'value': u'Futurist Painter Giacomo Balla', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1912', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-8162600', u'title': u"L'attrice fotodinamizzata", u'image': u'/media/get/12428/r-8162600/', u'thumbnail': u'/media/thumb/12428/r-8162600/', u'id': 12428, u'metadata': [{u'value': u'SL-20BRAA009', u'label': u'ID'}, {u'value': u"L'attrice fotodinamizzata", u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1913', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-5125511', u'title': u'Postcard with Anton Guilio Bragaglia Dressed as the Mona Lisa', u'image': u'/media/get/17370/r-5125511/', u'thumbnail': u'/media/thumb/17370/r-5125511/', u'id': 17370, u'metadata': [{u'value': u'AH-CD0000403-578', u'label': u'ID'}, {u'value': u'Postcard with Anton Guilio Bragaglia Dressed as the Mona Lisa', u'label': u'Title'}, {u'value': u'Mixed Media.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}]}, {u'name': u'r-4442993', u'title': u'Self Portrait', u'image': u'/media/get/21232/r-4442993/', u'thumbnail': u'/media/thumb/21232/r-4442993/', u'id': 21232, u'metadata': [{u'value': u'AH-CD0000406-515', u'label': u'ID'}, {u'value': u'Self Portrait', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1913', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}]}, {u'name': u'r-2595246', u'title': u'Thais, film still', u'image': u'/media/get/22062/r-2595246/', u'thumbnail': u'/media/thumb/22062/r-2595246/', u'id': 22062, u'metadata': [{u'value': u'AH-CD0000406-870', u'label': u'ID'}, {u'value': u'Thais, film still', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1917', u'label': u'Creation Year'}, {u'value': u'Film Still', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}]}, {u'name': u'r-2150930', u'title': u'The Writer Giannetto Bisi', u'image': u'/media/get/28148/r-2150930/', u'thumbnail': u'/media/thumb/28148/r-2150930/', u'id': 28148, u'metadata': [{u'value': u'AH-CD0000600-719', u'label': u'ID'}, {u'value': u'The Writer Giannetto Bisi', u'label': u'Title'}, {u'value': u'Bragaglia, Arturo', u'label': u'Creator'}, {u'value': u'1919', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-5027909', u'title': u'Self Portrait', u'image': u'/media/get/28151/r-5027909/', u'thumbnail': u'/media/thumb/28151/r-5027909/', u'id': 28151, u'metadata': [{u'value': u'AH-CD0000600-722', u'label': u'ID'}, {u'value': u'Self Portrait', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1914', u'label': u'Creation Year'}, {u'value': u'Postcard', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-5901135', u'title': u'Typist', u'image': u'/media/get/28152/r-5901135/', u'thumbnail': u'/media/thumb/28152/r-5901135/', u'id': 28152, u'metadata': [{u'value': u'AH-CD0000600-723', u'label': u'ID'}, {u'value': u'Typist', u'label': u'Title'}, {u'value': u'Anton Giulio and Arturo Bragaglia', u'label': u'Creator'}, {u'value': u'1913', u'label': u'Creation Year'}, {u'value': u'Postcard', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-2821954', u'title': u'Photodynamic Portrait of Anton Giulio Bragaglia', u'image': u'/media/get/28153/r-2821954/', u'thumbnail': u'/media/thumb/28153/r-2821954/', u'id': 28153, u'metadata': [{u'value': u'AH-CD0000600-724', u'label': u'ID'}, {u'value': u'Photodynamic Portrait of Anton Giulio Bragaglia', u'label': u'Title'}, {u'value': u'Bonaventura, Gustavo', u'label': u'Creator'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-1036216', u'title': u'Polyphysiognomical Porrait of Boccioni', u'image': u'/media/get/28154/r-1036216/', u'thumbnail': u'/media/thumb/28154/r-1036216/', u'id': 28154, u'metadata': [{u'value': u'AH-CD0000600-725', u'label': u'ID'}, {u'value': u'Polyphysiognomical Porrait of Boccioni', u'label': u'Title'}, {u'value': u'Anton Giulio and Arturo Bragaglia', u'label': u'Creator'}, {u'value': u'1913', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-4213053', u'title': u'Change of Position', u'image': u'/media/get/28155/r-4213053/', u'thumbnail': u'/media/thumb/28155/r-4213053/', u'id': 28155, u'metadata': [{u'value': u'AH-CD0000600-726', u'label': u'ID'}, {u'value': u'Change of Position', u'label': u'Title'}, {u'value': u'Anton Giulio Bragaglia', u'label': u'Creator'}, {u'value': u'1911', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-3446938', u'title': u'Futurist Gerardo Dottori', u'image': u'/media/get/28166/r-3446938/', u'thumbnail': u'/media/thumb/28166/r-3446938/', u'id': 28166, u'metadata': [{u'value': u'AH-CD0000600-737', u'label': u'ID'}, {u'value': u'Futurist Gerardo Dottori', u'label': u'Title'}, {u'value': u'Bragaglia, Arturo', u'label': u'Creator'}, {u'value': u'1920', u'label': u'Creation Year'}, {u'value': u'Photographic Construction', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-4522899', u'title': u'Photodynamic Portrait of a Woman', u'image': u'/media/get/28170/r-4522899/', u'thumbnail': u'/media/thumb/28170/r-4522899/', u'id': 28170, u'metadata': [{u'value': u'AH-CD0000600-741', u'label': u'ID'}, {u'value': u'Photodynamic Portrait of a Woman', u'label': u'Title'}, {u'value': u'Bragaglia, Arturo', u'label': u'Creator'}, {u'value': u'1924', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-3999353', u'title': u'Child', u'image': u'/media/get/28171/r-3999353/', u'thumbnail': u'/media/thumb/28171/r-3999353/', u'id': 28171, u'metadata': [{u'value': u'AH-CD0000600-742', u'label': u'ID'}, {u'value': u'Child', u'label': u'Title'}, {u'value': u'Bragaglia, Arturo', u'label': u'Creator'}, {u'value': u'1920', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-7492364', u'title': u'Polyphysiognomic Portrait', u'image': u'/media/get/28194/r-7492364/', u'thumbnail': u'/media/thumb/28194/r-7492364/', u'id': 28194, u'metadata': [{u'value': u'AH-CD0000600-765', u'label': u'ID'}, {u'value': u'Polyphysiognomic Portrait', u'label': u'Title'}, {u'value': u'Bragaglia, Arturo', u'label': u'Creator'}, {u'value': u'1930', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Futurism.', u'label': u'Style'}, {u'value': u'no', u'label': u'Copyright'}]}, {u'name': u'r-9793011', u'title': u'Thais, still', u'image': u'/media/get/35156/r-9793011/', u'thumbnail': u'/media/thumb/35156/r-9793011/', u'id': 35156, u'metadata': [{u'value': u'AH-CD0000606-930', u'label': u'ID'}, {u'value': u'Thais, still', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1916', u'label': u'Creation Year'}, {u'value': u'Film Still', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Italy', u'label': u'Country'}, {u'value': u'Centro Studi Bragaglia, Rome', u'label': u'Site'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-3402504', u'title': u'Thais, still', u'image': u'/media/get/35157/r-3402504/', u'thumbnail': u'/media/thumb/35157/r-3402504/', u'id': 35157, u'metadata': [{u'value': u'AH-CD0000606-931', u'label': u'ID'}, {u'value': u'Thais, still', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1916', u'label': u'Creation Year'}, {u'value': u'Film Still', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Italy', u'label': u'Country'}, {u'value': u'Centro Studi Bragaglia, Rome', u'label': u'Site'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-4336192', u'title': u'Thais, still', u'image': u'/media/get/35158/r-4336192/', u'thumbnail': u'/media/thumb/35158/r-4336192/', u'id': 35158, u'metadata': [{u'value': u'AH-CD0000606-932', u'label': u'ID'}, {u'value': u'Thais, still', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1916', u'label': u'Creation Year'}, {u'value': u'Film Still', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'Italy', u'label': u'Country'}, {u'value': u'Centro Studi Bragaglia, Rome', u'label': u'Site'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-7449455', u'title': u'Aerodance, Rosalia Chladek', u'image': u'/media/get/35257/r-7449455/', u'thumbnail': u'/media/thumb/35257/r-7449455/', u'id': 35257, u'metadata': [{u'value': u'AH-CD0000607-031', u'label': u'ID'}, {u'value': u'Aerodance, Rosalia Chladek', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1933', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-9859830', u'title': u'Aerodance, Rosalia Chladek', u'image': u'/media/get/35258/r-9859830/', u'thumbnail': u'/media/thumb/35258/r-9859830/', u'id': 35258, u'metadata': [{u'value': u'AH-CD0000607-032', u'label': u'ID'}, {u'value': u'Aerodance, Rosalia Chladek', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1933', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-7284766', u'title': u'Aerodance, Rosalia Chladek', u'image': u'/media/get/35259/r-7284766/', u'thumbnail': u'/media/thumb/35259/r-7284766/', u'id': 35259, u'metadata': [{u'value': u'AH-CD0000607-033', u'label': u'ID'}, {u'value': u'Aerodance, Rosalia Chladek', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1933', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-9973605', u'title': u'First Edition of Book by Anton Giulio Bragaglia', u'image': u'/media/get/35341/r-9973605/', u'thumbnail': u'/media/thumb/35341/r-9973605/', u'id': 35341, u'metadata': [{u'value': u'AH-CD0000607-115', u'label': u'ID'}, {u'value': u'First Edition of Book by Anton Giulio Bragaglia', u'label': u'Title'}, {u'value': u'Bragaglia, Anton Giulio', u'label': u'Creator'}, {u'value': u'1913', u'label': u'Creation Year'}, {u'value': u'Book Cover', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-6689389', u'title': u"Inauguration with Marinetti and the Futurists at the Casa d'Arte Bragaglia, Rome", u'image': u'/media/get/35347/r-6689389/', u'thumbnail': u'/media/thumb/35347/r-6689389/', u'id': 35347, u'metadata': [{u'value': u'AH-CD0000607-121', u'label': u'ID'}, {u'value': u"Inauguration with Marinetti and the Futurists at the Casa d'Arte Bragaglia, Rome", u'label': u'Title'}, {u'value': u'Bragaglia, Arturo', u'label': u'Creator'}, {u'value': u'1922', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Italian.', u'label': u'Culture'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'no', u'label': u'Copyright Permission'}]}, {u'name': u'r-8332348', u'title': u'The Smoker', u'image': u'/media/get/44196/r-8332348/', u'thumbnail': u'/media/thumb/44196/r-8332348/', u'id': 44196, u'metadata': [{u'value': u'AH-CD0000611-614', u'label': u'ID'}, {u'value': u'The Smoker', u'label': u'Title'}, {u'value': u'Anton Giulio and Arturo Bragaglia', u'label': u'Creator'}, {u'value': u'1913', u'label': u'Creation Year'}, {u'value': u'Silver gelatin print.', u'label': u'Medium'}, {u'value': u'Modern: 19th c. to present.', u'label': u'Period'}, {u'value': u'no', u'label': u'Copyright Permission'}]}], u'result': u'ok', u'hidden': False, u'id': 4970, u'name': u'futurism-bragaglia'}
Trying
	r-2250176
	SL-20BRAA001
ritratto polifisionomico
	r-6635695
	SL-20BRAA002
Young Man Swinging
	r-8183409
	SL-20BRAA003
Ducking
	r-6811396
	SL-20BRAA004
Greetings
	r-5137792
	SL-20BRAA005
dattilografa
	r-1403707
	SL-20BRAA006
Going Around
	r-7633456
	SL-20BRAA007
Futurist Painter Giacomo Balla
	r-7680059
	SL-20BRAA008
L'attrice fotodinamizzata
	r-8162600
	SL-20BRAA009
Postcard with Anton Guilio Bragaglia Dressed as the Mona Lisa
	r-5125511
	AH-CD0000403-578
Self Portrait
	r-4442993
	AH-CD0000406-515
Thais, film still
	r-2595246
	AH-CD0000406-870
The Writer Giannetto Bisi
	r-2150930
	AH-CD0000600-719
Self Portrait
	r-5027909
	AH-CD0000600-722
Typist
	r-5901135
	AH-CD0000600-723
Photodynamic Portrait of Anton Giulio Bragaglia
	r-2821954
	AH-CD0000600-724
Polyphysiognomical Porrait of Boccioni
	r-1036216
	AH-CD0000600-725
Change of Position
	r-4213053
	AH-CD0000600-726
Futurist Gerardo Dottori
	r-3446938
	AH-CD0000600-737
Photodynamic Portrait of a Woman
	r-4522899
	AH-CD0000600-741
Child
	r-3999353
	AH-CD0000600-742
Polyphysiognomic Portrait
	r-7492364
	AH-CD0000600-765
Thais, still
	r-9793011
	AH-CD0000606-930
Thais, still
	r-3402504
	AH-CD0000606-931
Thais, still
	r-4336192
	AH-CD0000606-932
Aerodance, Rosalia Chladek
	r-7449455
	AH-CD0000607-031
Aerodance, Rosalia Chladek
	r-9859830
	AH-CD0000607-032
Aerodance, Rosalia Chladek
	r-7284766
	AH-CD0000607-033
First Edition of Book by Anton Giulio Bragaglia
	r-9973605
	AH-CD0000607-115
Inauguration with Marinetti and the Futurists at the Casa d'Arte Bragaglia, Rome
	r-6689389
	AH-CD0000607-121
The Smoker
	r-8332348
	AH-CD0000611-614
total slides: 31

Process finished with exit code 0
"""