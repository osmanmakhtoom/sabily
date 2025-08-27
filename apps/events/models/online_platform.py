from django.core.validators import URLValidator
from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class OnlinePlatform(AllMixinInheritedMixin):
    name = models.CharField(max_length=255, db_index=True)
    website = models.URLField(validators=[URLValidator()])
    icon = models.ImageField(
        upload_to="online_event_platforms_icons/", null=True, blank=True
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
