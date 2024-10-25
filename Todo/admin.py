from django.contrib import admin
from . import models
# Register your models here.


class Todo_lists(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ['id','Title','completed','Date',"Description"]
    list_filter=['user','completed','Title','id']  
    # Enable search functionality
    search_fields =['Title']

admin.site.register(models.Todo_list,Todo_lists)

admin.site.site_header='Simorg Todo'
admin.site.site_title="TODO"