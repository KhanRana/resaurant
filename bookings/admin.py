from django.contrib import admin
from .models import Menu, Review, Booking, Table
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','created_on')
    list_filter = ('created_on',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'email', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields= ('name', 'body', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'no_of_persons', 'date', 'time')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('num', 'capacity')