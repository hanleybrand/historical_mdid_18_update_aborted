from __future__ import with_statement, absolute_import
from datetime import datetime  # , timedelta
import logging
import os
# import uuid
import mimetypes
import json

from django import forms
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group
from django.core.urlresolvers import resolve, reverse
from django.forms.util import ErrorList
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseForbidden
# HttpResponseServerError
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response  # _get_queryset,
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import filesizeformat

from rooibos.access import filter_by_access
from rooibos.data.models import Collection
from .models import Storage, Media
from .views import make_storage_select_choice

log = logging.getLogger(__name__)

available_collections = get_list_or_404(filter_by_access(request.user, Collection))
writable_collection_ids = list(filter_by_access(request.user, Collection, write=True).values_list('id', flat=True))

class ChoiceForm(forms.Form):
    pass


class UploadFileForm(forms.Form):
    pass
    #
    # collection = forms.ChoiceField(
    #     choices=((c.id,
    #               '%s%s' % ('*' if c.id in list(
    #                                 filter_by_access(user,
    #                                                  Collection,
    #                                                  write=True).values_list('id', flat=True))
    #                             else '', c.title)) for c in
    #              sorted(available_collections, key=lambda c: c.title)))
    # storage = forms.ChoiceField(choices=storage_choices)
    # file = forms.FileField()
    # create_records = forms.BooleanField(required=False)
    # replace_files = forms.BooleanField(required=False, label='Replace files of same type')
    # multiple_files = forms.BooleanField(required=False,
    #                                     label='Allow multiple files of same type')
    # personal_records = forms.BooleanField(required=False)
    #
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super(UploadFileForm, self).__init__(*args, **kwargs)
    #
    # # NO, this is not it
    # def available_storage(user):
    #     return list(filter_by_access(user, Collection, write=True).values_list('id', flat=True))
    #
    # def available_collections(user):
    #     return get_list_or_404(filter_by_access(user, Collection))
    #
    # def storage_choices(user):
    #     return [make_storage_select_choice(s, request.user) for s in available_storage]
    #
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     if any(self.errors):
    #         return cleaned_data
    #     personal = cleaned_data['personal_records']
    #     if not personal:
    #         if not int(cleaned_data['collection']) in writable_collection_ids:
    #             self._errors['collection'] = ErrorList(["Can only add personal records to selected collection"])
    #             del cleaned_data['collection']
    #     return cleaned_data