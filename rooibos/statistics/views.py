# Create your views here.
from __future__ import absolute_import

from django.shortcuts import render
from django_tables2 import RequestConfig
from django_tables2 import SingleTableView

from .functions import fake_distinct
from .models import Activity
from .tables import ActivityTable


# see http://django-tables2.readthedocs.org/en/latest/index.html
# for more details, but there's an FBV and CBV here
# url: stats.full_table
def activity_table(request):
    table = ActivityTable(Activity.objects.all())
    event_types = Activity.objects.values_list('event')

    # filter.distinct() doesn't work with mysql because #$%#@$%#


    RequestConfig(request).configure(table)
    RequestConfig(request, paginate={"per_page": 50}).configure(table)

    return render(request,
                  'activity_table_view.html',
                  {'table': table,
                   'event_types': fake_distinct(Activity, 'event')})


class EventList(SingleTableView):
    model = Activity
    table_pagination = {'per_page': 50}
    template_name = 'activity_table_view.html'
    table_class = ActivityTable

    def get_queryset(self):
        # self.args[0] in this case would be /stats/events/{self.args[0]}
        # e.g. /stats/events/login
        return Activity.objects.filter(event=self.args[0])


# basic django-tables2 view
# class ActivityTableView(SingleTableView):
# model = Activity
# table_class = ActivityTable
#     template_name = 'activity_table_view.html'
#

# deleted urls
# urls: stats_table/username/<query>/ , {'field': 'username'}
# this doesn't work like I assumed it would...
# def filtered_table(request, field, query):
#     if query:
#         if field == 'username':
#             user_pk = User.objects.get(username=query).id
#             table = Activity.objects.filter(user_field=user_pk)
#         if field == 'event':
#             table = Activity.objects.filter(event=query)
#         if field == 'data':
#             table = Activity.objects.filter(data_field=query)
#         # else:
#         #     table = Activity.objects.filter(Q(Activity.objects.get(event__contains=query)) |
#         #                                     Activity.objects.filter(data_field__contains=query))
#
#         RequestConfig(request).configure(table)
#         RequestConfig(request, paginate={"per_page": 50}).configure(table)
#
#         return render(request,
#                       'activity_table_view.html',
#                       {'table': table,
#                        'filtered_field': field,
#                        'query': query})
#
#     else:
#         return HttpResponseRedirect(reverse('stats.full_table'))


# class ActivityList(ListView):
# model = Activity
# context_object_name = 'statistics'
# table = ActivityTable(Activity.objects.all())


# This also doesn't work so well... hmmmm
# class FilteredTableView(SingleTableView):
#     model = Activity
#     table_class = ActivityTable
#     hide_media_activity = False
#
#     def get_queryset(self):
#         if not self.args[1]:
#             return Activity.objects.filter(Q(Activity.objects.filter(event=self.args[0])) |
#                                            Activity.objects.filter(data_field=self.args[0]))
#         if self.args[0] == 'username':
#             user_pk = User.objects.get(username=self.args[1]).id
#             return Activity.objects.filter(user_field=user_pk)
#         if self.args[0] == 'event':
#             return Activity.objects.filter(event=self.args[1])
#         if self.args[0] == 'data':
#             return Activity.objects.filter(data_field=self.args[1])
#         else:
#             return HttpResponseRedirect(reverse('stats.full_table'))


