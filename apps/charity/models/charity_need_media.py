from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class CharityNeedMedia(AllMixinInheritedMixin):
    need = models.ForeignKey(
        "CharityNeed", on_delete=models.CASCADE, related_name="media"
    )
    image = models.ImageField(upload_to="charity_need_media/", null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["id", "-is_active", "-created_at"]

    def __str__(self):
        return f"Image {self.order} - {self.need}"
