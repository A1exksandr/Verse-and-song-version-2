from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.author_list, name="author_list"),
    path("authors/<slug:slug>/", views.author_detail, name="author_detail"),
    path("works/", views.work_list, name="work_list"),
    path("works/<slug:slug>/", views.work_detail, name="work_detail"),
    path("genres/", views.genre_list, name="genre_list"),
    path("about/", views.about, name="about"),
    path("search/", views.search, name="search"),
]
