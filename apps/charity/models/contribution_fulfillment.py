from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class ContributionFulfillment(AllMixinInheritedMixin):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=64)
    contribution = GenericForeignKey("content_type", "object_id")
    need = models.ForeignKey(
        "CharityNeed", on_delete=models.PROTECT, related_name="fulfillments"
    )
    quantity_applied = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
            models.Index(fields=["need"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.contribution} → {self.need} ({self.quantity_applied})"

    @property
    def contribution_type(self):
        return self.content_type.model_class().__name__

    def save(self, *args, **kwargs):
        if self.quantity_applied > self.need.remaining_quantity:
            raise ValidationError("Applied quantity exceeds need remaining")
        super().save(*args, **kwargs)
