from __future__ import with_statement
import json
from rooibos.workers import register_worker
from rooibos.workers.models import JobInfo
from rooibos.data.models import Collection, FieldSet
import logging
import os
import csv
from spreadsheetimport import SpreadsheetImport
from views import _get_scratch_dir
import traceback

log = logging.getLogger(__name__)

@register_worker('csvimport')
def csvimport(job):

    log.debug('csvimport started for %s' % job)
    jobinfo = JobInfo.objects.get(id=job.arg)

    try:

        arg = json.loads(jobinfo.arg)

        if jobinfo.status.startswith == 'Complete':
            # job finished previously
            log.debug('csvimport finished previously for %s' % job)
            return

        file = os.path.join(_get_scratch_dir(), arg['file'])
        if not os.path.exists(file):
            # import file missing
            log.exception('Import file %s missing', file)
            jobinfo.complete('Import file missing', 'Import failed')

        resultfile = file + '.result'
        if os.path.exists(resultfile):
            # import must have died in progress
            with open(resultfile, 'r') as f:
                results = csv.DictReader(f)
                count = -1
                for count, row in enumerate(results):
                    pass
            skip_rows = count + 1
        else:
            skip_rows = 0

        infile = open(file, 'rU')
        outfile = open(resultfile, 'a', 0)
        outwriter = csv.writer(outfile)

        if not skip_rows:
            outwriter.writerow(['Identifier', 'Action'])

        class Counter(object):
            def __init__(self):
                self.counter = 0

        def create_handler(event, counter_obj):
            # TODO: pycharm is raising 'unresolved reference' errors for counter -
            # it's dumb, but I guess it what ws happening confused me for a second
            # so I refactored the funcion arg to be counter_obj, to make clear that
            # a Counter is being passed
            def handler(id):
                counter_obj.counter += 1
                jobinfo.update_status('processing row %s' % counter_obj.counter)
                outwriter.writerow([';'.join(id) if id else '', event])

            log.debug('create_handler:  %s' % handler)
            return handler

        counter = Counter()
        handlers = dict(
            (e, create_handler(e, counter)) for e in SpreadsheetImport.events)

        fieldset = FieldSet.objects.filter(
            id=arg['fieldset']) if arg['fieldset'] else None

        collections = Collection.objects.filter(id__in=arg['collections'])

        imp = SpreadsheetImport(
            infile,
            collections,
            separator=arg['separator'],
            owner=jobinfo.owner if arg['personal'] else None,
            preferred_fieldset=fieldset[0] if fieldset else None,
            mapping=arg['mapping'],
            separate_fields=arg['separate_fields'],
            labels=arg['labels'],
            order=arg['order'],
            hidden=arg['hidden'],
            **handlers
        )

        log.debug('csvimport calling run() for %s' % job)
        log.debug('skip_rows = %s' % skip_rows)
        imp.run(arg['update'],
                arg['add'],
                arg['test'],
                collections,
                skip_rows=skip_rows)

        log.info('csvimport complete: %s' % job)

        jobinfo.complete('Complete', '%s rows processed' % counter.counter)

    except Exception as ex:
        log.exception('csvimport failed: %s' % job)
        log.exception(traceback.format_exc())
        jobinfo.complete('Failed: %s\n%s' % (ex, traceback.format_exc()), None)
