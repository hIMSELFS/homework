from django.contrib import admin

from .models import *

class AdminItems(admin.ModelAdmin):
    list_display = ('id','shortName','shortText', 'price','uniUrl')
    search_fields = ('id','shortName','price')
    prepopulated_fields = {"uniUrl": ("shortName",)}
admin.site.register(Items,AdminItems)

class AdminCategory(admin.ModelAdmin):
    list_display = ('id','category','uniCat')
    search_fields = ('id','category','uniCat')
    prepopulated_fields = {"uniCat": ("category",)}
admin.site.register(category,AdminCategory)
