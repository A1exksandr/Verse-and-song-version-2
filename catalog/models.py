from django.db import models


class Author(models.Model):
    class Category(models.TextChoices):
        POET = "poet", "Поэт"
        MUSICIAN = "musician", "Музыкант"
        BAND = "band", "Группа"
        WRITER = "writer", "Писатель"

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        allow_unicode=True,
    )
    image = models.ImageField(upload_to="authors/", blank=True)
    category = models.CharField(
        max_length=20,
        choices=Category,
        default=Category.POET,
    )
    start_date = models.DateField(
        blank=True,
        null=True,
        help_text="Дата рождения или основания группы",
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="Дата смерти или распада группы",
    )
    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        allow_unicode=True,
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="genres/", blank=True)

    def __str__(self):
        return self.name


class Work(models.Model):
    class WorkType(models.TextChoices):
        POEM = "poem", "Стихотворение"
        SONG = "song", "Песня"

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        allow_unicode=True,
    )
    work_type = models.CharField(
        max_length=20,
        choices=WorkType,
    )
    text = models.TextField(blank=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="works",
    )
    genres = models.ManyToManyField(
        Genre,
        blank=True,
        related_name="works",
    )

    publication_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="works/", blank=True)
    audio = models.FileField(upload_to="audio/", blank=True)
    duration = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Продолжительность в секундах",
    )
    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title