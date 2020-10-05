from django.contrib import admin


class ModelVersionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'

    search_fields = [
        'model__name',
        'version',
    ]

    list_display = [
        'id',
        'model',
        'version',
    ]

    list_display_links = [
        'id',
        'version',
    ]

    autocomplete_fields = [
        'model',
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
                ('model', 'version',),
            )
        }),
        ('Creation', {
            'fields': (
                ('created_on', 'created_by'),
                ('modified_on', 'modified_by'),
            )
        }),
    )
