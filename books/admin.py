from django.contrib import admin

from django.forms import TextInput, Textarea
from django.db import models

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('bookname', 'author', 'year', 'pages', 'comment', 'registered')
    list_display_links = ('bookname', 'author')
    search_fields = ('bookname', 'author', 'comment')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        # models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


admin.site.register(Book, BookAdmin)
