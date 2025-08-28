from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Tag(AllMixinInheritedMixin):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
