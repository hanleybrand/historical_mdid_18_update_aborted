from django.contrib import admin
from models import MetadataStandard, Field, FieldSet, FieldSetField, Record, FieldValue, Collection

class MetadataStandardAdmin(admin.ModelAdmin):
    pass


class FieldAdmin(admin.ModelAdmin):
    list_filter = ('standard', )
    #raw_id_fields = ('equivalent')
    list_display = ('name', 'label', 'standard', 'vocabulary', 'old_name',  )



class FieldSetFieldInline(admin.TabularInline):
    model = FieldSetField


class FieldSetAdmin(admin.ModelAdmin):
    inlines = [FieldSetFieldInline,]


class FieldValueInline(admin.TabularInline):
    model = FieldValue
    raw_id_fields = ['owner', 'context_type',]

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified',  )
    list_filter = ['created', 'modified',]
    search_fields = ['name',]
    inlines = [FieldValueInline,]
    pass


class CollectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Collection, CollectionAdmin)
admin.site.register(MetadataStandard, MetadataStandardAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(FieldSet, FieldSetAdmin)
admin.site.register(Record, RecordAdmin)

