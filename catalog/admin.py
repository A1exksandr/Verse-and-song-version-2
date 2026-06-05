from django.contrib import admin

from .models import Author, Genre, Work

@admin.register(Work)
class WorkDoing(Work):
    pass