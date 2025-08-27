from django.conf import settings
from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Photo(AllMixinInheritedMixin):
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="event_gallery/")
    caption = models.CharField(max_length=200, blank=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="uploaded_event_photos",
    )

    def __str__(self):
        return f"Photo for {self.event}"
