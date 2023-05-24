from django.contrib import admin
from .models import Menu
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    list_filter = ('created_on',)
    summernote_fields = ('content')
