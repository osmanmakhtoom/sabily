from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class CharityType(AllMixinInheritedMixin):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to="charity_types_icons/", blank=True)

    class Meta:
        ordering = ["id", "name", "-created_at", "-updated_at"]

    def __str__(self):
        return f"{self.name}"
