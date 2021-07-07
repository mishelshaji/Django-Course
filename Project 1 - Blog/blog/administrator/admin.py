from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name','description', 'color')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name', 'color')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title', 'slug', 'category')
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title', 'category')