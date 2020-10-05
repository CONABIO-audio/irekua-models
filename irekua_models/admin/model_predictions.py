from django.contrib import admin


class ModelPredictionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'

    search_fields = [
        'pk',
    ]

    list_display = [
        'id',
        'item',
        'event_type',
        'annotation_type',
        'certainty',
        'created_by',
        'created_on',
    ]

    list_filter = [
        'event_type',
        'certainty',
        'annotation_type',
    ]

    autocomplete_fields = [
        'item',
        'event_type',
        'model_version',
        'labels',
    ]

    readonly_fields = [
        'created_on',
        'modified_on',
        'created_by',
        'modified_by',
    ]

    fieldsets = (
        (None, {
            'fields': (
                ('item', 'model_version',),
                ('event_type', 'annotation_type', 'certainty'),
                ('annotation', 'labels',),
            )
        }),
        ('Creation', {
            'fields': (
                ('created_on', 'created_by'),
                ('modified_on', 'modified_by'),
            )
        }),
    )
