from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class Teamadmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'
    list_display = ('id','thumbnail','first_name','last_name','designation','created_date')
    list_display_links = ('id','thumbnail','first_name',)
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)

admin.site.register(Team,Teamadmin)
# Register your models here.
