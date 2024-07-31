from django.contrib import admin
from . import models

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','authors']
    search_fields = ('title',)

admin.site.register(models.Book, BookAdmin)