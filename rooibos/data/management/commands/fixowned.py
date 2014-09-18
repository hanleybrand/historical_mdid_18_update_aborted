import sys
import csv
import mimetypes

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from django.core.files import File
from django.db.models import Q

from rooibos.data.models import Record, standardfield, Field, FieldValue, Collection, CollectionItem
from rooibos.storage.models import Media, Storage
from rooibos.storage import get_media_for_record


class Command(BaseCommand):
    help = """options: 'path/to/file.csv'

    Open a csv of owned records and their media files. Acquire with this sql for now:

    SELECT
        data_record.owner_id,
        data_record.id as record_id,
        data_record.name as record_name,
        storage_media.url as file_path,
        TRIM(LEADING 'full/' FROM storage_media.url) as file_name,
        TRIM(TRAILING '.jpg' FROM TRIM(LEADING 'full/' FROM storage_media.url)) as file_identifier
    FROM
        data_record
            join
        storage_media ON storage_media.record_id = data_record.id
    WHERE
        data_record.owner_id is not NULL"""

    def handle(self, *args, **options):

        #print sys.argv
        # if you want to restrict from one storage, define here
        use_storage = Storage.objects.get(name='personal-images')
        server_url = 'https://gallery.temple.edu'

        csv_infile = open(sys.argv[2], 'rt')
        rows_total = 0
        rows_processed = 0
        rows_fixed = 0
        # csv_outfile = open('fixowned_out.csv')

        try:
            fid, fid_created = Field.objects.get_or_create(label='Uploaded File Name')
            want_hidden = False

            hide = 'y'
            if hide == 'y':
                want_hidden = True

            row_counter = csv.DictReader(csv_infile)


            # writer = csv.DictWriter(csv_outfile)
            for row in row_counter:
                rows_total += 1

            csv_infile = open(sys.argv[2], 'rt')
            reader = csv.DictReader(csv_infile)
            print '\nStarting record fix -  %i rows read' % (rows_total)

            for order, row in enumerate(reader):

                #rec = Record.objects.get(name=row['record_name'])

                try:
                    rec = Record.objects.get(name=row['record_name'])
                except ObjectDoesNotExist:
                    print 'record %s does not exist' % row['record_name']
                    break
                except Exception as e:
                    print e
                    break

                rec_url = server_url + rec.get_absolute_url()
                file_path = row['file_path']
                print 'row: %s _________ rec %s ____________________________________' % (order, rec.id)
                #print rec.title
                #print server_url + rec.get_absolute_url()
                #print file_path
                #print rec.get_fieldvalues(hide_default_data=True)

                # if record has Uploaded File field, update hidden pref
                # if there's more than one, sk to delete
                try:
                    fix_field = rec.fieldvalue_set.filter(field=fid)
                    # print 'fix_fled = %s' % fix_field
                    if fix_field:
                        for fix in fix_field:
                            if len(fix.value) < 1:
                                raw_input('Should %s with value of \'%s\' be deleted? (y/n)' % (fix, fix.value))
                            else:
                                fix.hidden = want_hidden
                                fix.save()
                    else:
                        print 'setting hidden = True for %s' % rec_url

                except ObjectDoesNotExist:
                    fix_field = FieldValue.objects.create(record=rec,
                                                          field=fid,
                                                          value=file_path,
                                                          hidden=want_hidden)
                    print 'created %s' % fix_field

                # search all Storage objects and if the file is found, re-add a media record
                # if it doesn't have one
                img = None
                media_rec = None
                media_exists = None
                # try and get teh media record
                try:
                    media_rec = Media.objects.filter(record=rec)[0]
                except IndexError:
                    #print 'index error - trying get'

                #     print 'mult obj returned'
                    try:
                        media_rec = Media.objects.get(record=rec)
                    except ObjectDoesNotExist:
                        #print 'media ObjectDoesNotExist'
                        pass
                # except MultipleObjectsReturned:
                # #     print 'mult obj returned'
                # #     media_rec = Media.objects.get(record=rec)[0]


                # make sure that the file is really there
                if media_rec and media_rec.file_exists():
                    pass
                else:
                    # if the file isn't there, make a new media record
                    # check to see if an image exists in either a chosen storage or in any storage
                    if use_storage:
                        store = use_storage
                        print 'storage path = %s, file_path = %s' % (store.base, file_path)
                        try:
                            img = store.load_file(file_path)
                            print img
                            #use_storage = stores[order]
                            #print 'storage = %s, file_path = %s' % (use_storage, file_path)
                        except IOError as e:
                            print 'IOERROR ~ %s%s' % (store.base, file_path)
                            pass
                    else:
                        stores = Storage.objects.all()
                        for order, store in enumerate(stores):
                            # because a personal record can use whatever storage a user can write to
                            try:
                                img = store.load_file(file_path)
                                #use_storage = stores[order]
                                print 'storage = %s, file_path = %s' % (use_storage, file_path)

                            except IOError as e:
                                print '!!!!! IOERROR !!!!!'
                                print e
                                pass
                    try:
                        if img:
                            mimetype = mimetypes.guess_type(img.name)[0]
                            media_rec = Media.objects.create(record=rec,
                                                             storage=use_storage,
                                                             url=file_path,
                                                             mimetype=mimetype)
                            #print 'creating media %s for record %s' % (m.name, rec.name)
                            rows_fixed += 1
                    except Exception as e:
                        print '** UNABLE TO CREATE MEDIA RECORD **'
                        print e
                        pass
                if media_rec:
                    print 'record %s paired with media:  %s' % (
                    rec_url, server_url + media_rec.get_absolute_url())
                else:
                    print '^^^^^^^'

                rows_processed += 1

        except Exception as e:
            print e

        finally:
            print '\nOwned record fix complete - %i of %i processed, %i rows fixed\n' % (rows_processed, rows_total, rows_fixed)
            csv_infile.close()

