from rooibos.data.models import Record
from rooibos.storage.models import Media
from rooibos.workers import register_worker
from rooibos.workers.models import JobInfo
from rooibos.federatedsearch.flickr import FlickrSearch
from rooibos.util import guess_extension
import logging
import urllib2
import json

# unused imports
# import json
# import mimetypes
# import traceback

log = logging.getLogger(__name__)

@register_worker('flickr_download_media')
def flickr_download_media(job):
    log.info('flickr_download_media started for %s' % job)
    jobinfo = JobInfo.objects.get(id=job.arg)

    try:
        if jobinfo.status.startswith == 'Complete':
            # job finished previously
            return
        flickr = FlickrSearch()
        arg = json.loads(jobinfo.arg)
        record = Record.objects.get(id=arg['record'], manager='flickr')
        url = arg['url']
        storage = flickr.get_storage()
        file = urllib2.urlopen(url)
        setattr(file, 'size', int(file.info().get('content-length')))
        mimetype = file.info().get('content-type')
        media = Media.objects.create(record=record,
                                     storage=storage,
                                     name=record.name,
                                     mimetype=mimetype)
        media.save_file(record.name + guess_extension(mimetype), file)
        jobinfo.complete('Complete', 'File downloaded')

    except Exception, ex:
        log.info('flickr_download_media failed for %s (%s)' % (job, ex))
        jobinfo.update_status('Failed: %s' % ex)
