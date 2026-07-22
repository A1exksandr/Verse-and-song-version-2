from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Author, Genre, Work


def index(request):
    featured_poems = Work.objects.filter(
        featured=True,
        work_type=Work.WorkType.POEM,
    ).select_related("author")[:4]

    featured_songs = Work.objects.filter(
        featured=True,
        work_type=Work.WorkType.SONG,
    ).select_related("author")[:4]

    authors = Author.objects.all()[:4]

    context = {
        "featured_poems": featured_poems,
        "featured_songs": featured_songs,
        "authors": authors,
    }   

    return render(
        request,
        "catalog/index.html",
        context,
    )

def author_list(request):
    authors = Author.objects.all()
    return render(request, "catalog/author_list.html", {"authors": authors})


def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    works = author.works.all()
    return render(request, "catalog/author_detail.html", {
        "author": author,
        "works": works,
    })


def work_list(request):
    works = Work.objects.select_related("author").all()
    return render(request, "catalog/works_list.html", {"works": works})


def work_detail(request, slug):
    work = get_object_or_404(
        Work.objects.select_related("author").prefetch_related("genres"),
        slug=slug,
    )
    return render(request, "catalog/work_detail.html", {"work": work})


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, "catalog/genres.html", {"genres": genres})

def about(request):
    return render(request, "catalog/about.html")

def search(request):
    query = request.GET.get("q", "").strip()

    results = []

    if query:
        normalized_query = query.casefold()

        works = Work.objects.select_related("author").all()

        for work in works:
            title = work.title.casefold()
            text = (work.text or "").casefold()
            author = work.author.name.casefold()

            if (
                normalized_query in title
                or normalized_query in text
                or normalized_query in author
            ):
                results.append(work)

    return render(
        request,
        "catalog/search_results.html",
        {
            "query": query,
            "results": results,
        },
    )

def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    works = genre.works.select_related("author").all()

    return render(request, "catalog/genre_detail.html", {
        "genre": genre,
        "works": works,
    })