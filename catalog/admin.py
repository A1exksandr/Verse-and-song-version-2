from django.contrib import admin
from .models import Author, Genre, Work

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Work)