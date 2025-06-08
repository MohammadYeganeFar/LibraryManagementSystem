from django.contrib import admin
from library import models as lib_models

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'ISBN']
    filter_horizontal = ['authors']


class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'member', 'loan_date', 'return_date']
    date_hierarchy = 'loan_date'
    search_fields = ['book', 'member']


admin.site.register(lib_models.Book, BookAdmin)
admin.site.register(lib_models.Author, AuthorAdmin)
admin.site.register(lib_models.Member, MemberAdmin)
admin.site.register(lib_models.BorrowedBook, BorrowedBookAdmin)