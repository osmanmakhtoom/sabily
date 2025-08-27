from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class EventType(AllMixinInheritedMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to="event_type_icons/", blank=True, null=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
