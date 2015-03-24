from __future__ import with_statement, absolute_import
from rooibos.contrib.pyPdf.pdf import PdfFileReader

# from django.shortcuts import get_list_or_404
# from rooibos.access import filter_by_access
# from rooibos.data.models import Collection
# from .models import Storage


# def available_collections_storage(user):
#     """
#     Get collections & storage available to a particular user. Returns two variables, so use like:
#         collections, storage = available_collections_storage(request.user)
#     :param user: normally request.user, but any valid django object should work, e.g.
#         collections, storage = available_collections_storage(User.get_objects(pk=3))
#     :return:
#     """
#     available_storage = get_list_or_404(filter_by_access(user,
#                                                          Storage,
#                                                          manage=True).order_by('title').values_list('id',
#                                                                                                     'title'))
#     available_collections = get_list_or_404(filter_by_access(user,
#                                                              Collection,
#                                                              manage=True))
#     return available_collections, available_storage


def extractTextFromPdfStream(stream):
    reader = PdfFileReader(stream)
    return '\n'.join(reader.getPage(i).extractText()
                    for i in range(reader.getNumPages()))

def extractTextFromPdfFile(filename):
    with open(filename, 'rb') as stream:
        return extractTextFromPdfStream(stream)
