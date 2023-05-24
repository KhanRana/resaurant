from django.contrib import admin
from .models import Menu
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    search_fields = ('title',)
    list_display = ('title','created_on')
    list_filter = ('created_on',)
    summernote_fields = ('content')
