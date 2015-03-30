from __future__ import absolute_import

from django.contrib import admin

from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'user_field', 'event', 'data_field')
    list_filter = ('event', 'user_field')
    date_hierarchy = 'date'
    search_fields = ['user_field__username','event', 'data_field']
    ordering = ('-date', '-time')
    readonly_fields = (
        'content_type', 'object_id', 'content_object',
        'date', 'time', 'user_field', 'event', 'data_field')
    change_list_filter_template = "admin/filter_listing.html"

admin.site.register(Activity, ActivityAdmin)