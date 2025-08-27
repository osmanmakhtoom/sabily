from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Speaker(AllMixinInheritedMixin):
    name = models.CharField(max_length=200, db_index=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="events_speakers_photos/", blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
