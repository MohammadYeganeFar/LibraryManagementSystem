from django.contrib import admin
from library import models as lib_models

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['books']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'ISBN']
    filter_horizontal = ['authors']

admin.site.register(lib_models.Book, BookAdmin)
admin.site.register(lib_models.Author, AuthorAdmin)
admin.site.register(lib_models.Member, MemberAdmin)