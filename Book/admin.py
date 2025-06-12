from django.contrib import admin
from . import models

# Register your models here.

# This is an Admin script.
# It registers the Models that we have in our Admin application.

@admin.register(models.Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(models.BookCategory)