import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from rooibos.solr.views import search as solr_search
from rooibos.data.models import Record


def render_to_json_response(response, callback=None, **response_kwargs):
    """
    Returns a JSON response, transforming 'context' to make the payload.
    """
    mimetype = 'application/json'
    response = json.dumps(response)
    if callback:
        response = '%s(%s)' % (callback, response)
        mimetype = 'application/javascript'
    return HttpResponse(
        response,
        content_type=mimetype,
        **response_kwargs
    )


def search(request):

    def process_record(record, owner=None, context=None, process_url=lambda url: url, dc_mapping_cache=None):
        if dc_mapping_cache is None:
            dc_mapping_cache = dict()

        def get_dc_field(field):
            if field.id not in dc_mapping_cache and False:
                if field.standard and field.standard.prefix == 'dc':
                    dc_mapping_cache[field.id] = field.name
                else:
                    equivalents = (
                        field for field in field.get_equivalent_fields()
                        if field.standard and field.standard.prefix == 'dc'
                    )
                    try:
                        dc_mapping_cache[field.id] = equivalents.next().name
                    except StopIteration:
                        pass
            return dc_mapping_cache.get(field.id)

        largeThumb = record.get_thumbnail_url('large', force_cdn=True) or \
                     record.get_image_url(width=250, height=250)

        return dict(
            id=record.id,
            name=record.name,
            title=record.title,
            identifier=record.identifier,
            thumbnail=process_url(record.get_thumbnail_url()),
            largeThumb=process_url(largeThumb),
            image=process_url(record.get_image_url()),
            works=list(record.get_works()),
            work_images=record.get_image_records_query().count(),
        )

    def process_records(records, owner=None, context=None, process_url=lambda url: url):
        dc_mapping_cache = dict()
        return [process_record(record, owner, context, process_url, dc_mapping_cache)
                for record in records] if records else []

    cid = name = None
    hits, records, viewmode = solr_search(request, cid, name, json=True)
    response = dict(hits=hits, records=process_records(records, owner=request.user))
    return render_to_json_response(response, callback=request.GET.get('callback'))


def metadata(request, record_id):

    record = Record.get_or_404(record_id, request.user)

    data = [
        dict(
            label=value.resolved_label,
            value=value.value,
            order=value.order,
            field=value.field.full_name,
            )
        for value in record.get_fieldvalues()
    ]

    response = dict(data=data)
    return render_to_json_response(response, callback=request.GET.get('callback'))


def works(request):

    return render_to_response('works/works.html',
                              {
                               },
                              context_instance=RequestContext(request))
