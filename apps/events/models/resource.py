from django.conf import settings
from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Resource(AllMixinInheritedMixin):
    event = models.ForeignKey(
        "Event", on_delete=models.CASCADE, related_name="resources"
    )
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to="event_resources/")
    is_public = models.BooleanField(default=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="uploaded_event_resources",
    )

    def __str__(self):
        return self.name
