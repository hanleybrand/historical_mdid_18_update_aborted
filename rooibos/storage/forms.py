# for implementing django forms
from __future__ import absolute_import
from django.forms import ModelForm

from .models import Storage


# example form for file uploading
class StorageForm(ModelForm):

    class Meta:
        model = Storage
        # never under any circumstances let someone set 'derivatve'
        fields = ['title', 'system', 'base', 'urlbase', 'deliverybase']

