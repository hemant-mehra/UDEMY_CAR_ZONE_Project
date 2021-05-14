from django.contrib import admin
from pages import models
from django.utils.html import format_html
# Register your models here.

"""customization in Team admin"""


class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius :40px;"/>')

    thumbnail.short_description = 'Photo'

    list_display = (
        'id', 'thumbnail', 'first_name', 'designation', 'created_date',
    )

    list_display_links = (
        'id', 'thumbnail', 'first_name',
    )

    search_fields = ('first_name', 'last_name', 'designation',)

    list_filter = (
        'designation',
    )

admin.site.register(models.Team, TeamAdmin)
