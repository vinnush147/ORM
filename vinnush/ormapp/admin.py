from django.contrib import admin
from .models import books_DB,books_DBAdmin
admin.site.register(books_DB,books_DBAdmin)