from django.contrib import admin
from .models import Menu, Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    search_fields = ('title',)
    list_display = ('title','created_on')
    list_filter = ('created_on',)
    summernote_fields = ('content')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'email', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields= ('name', 'body', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
