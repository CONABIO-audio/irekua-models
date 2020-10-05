from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from irekua_models import models


class VersionsInline(admin.TabularInline):
    extra = 0
    model = models.ModelVersion
    verbose_name = _('Version')
    verbose_name_plural = _('Versions')


class ModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'

    search_fields = [
        'name',
        'description',
    ]

    list_display = [
        'id',
        'name',
        'annotation_type',
        'created_on',
        'created_by',
    ]

    list_display_links = [
        'id',
        'name',
    ]

    autocomplete_fields = [
        'annotation_type',
        'item_types',
        'event_types',
        'terms',
    ]

    list_filter = [
        'annotation_type',
        'item_types',
        'event_types',
    ]

    readonly_fields = [
        'created_on',
        'created_by',
        'modified_on',
        'modified_by',
    ]

    fieldsets = (
        (None, {
            'fields': (
                ('name', 'annotation_type',),
                ('description',),
                ('repository',),
            )
        }),
        ('Configuration', {
            'classes': ('collapse', ),
            'fields': (
                ('item_types', 'event_types'),
                ('terms',),
            )
        }),
        ('Creation', {
            'fields': (
                ('created_on', 'created_by'),
                ('modified_on', 'modified_by'),
            )
        }),
    )

    inlines = [
        VersionsInline,
    ]
