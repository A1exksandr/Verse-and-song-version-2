from django.db import models

class Author(models.Model):
    ...


class Genre(models.Model):
    ...

# Черновик модели Work.
# Может измениться после проектирования ER-диаграммы.
class Work(models.Model):
    POEM = "poem"
    SONG = "song"

    WORK_TYPES = [
        (POEM, "Стихотворение"),
        (SONG, "Песня"),
    ]

    title = models.CharField(max_length=255)
    work_type = models.CharField(max_length=20, choices=WORK_TYPES)
    text = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="works")
    genres = models.ManyToManyField(Genre, blank=True, related_name="works")

    audio = models.FileField(upload_to="audio/", blank=True, null=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    def has_audio(self):
        return bool(self.audio)

    def is_song(self):
        return self.work_type == self.SONG

    def is_poem(self):
        return self.work_type == self.POEM