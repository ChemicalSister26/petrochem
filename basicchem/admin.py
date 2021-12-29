from django.contrib import admin

from .models import *

admin.site.register(Basicchem)

admin.site.register(Category)

class BasicchemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}