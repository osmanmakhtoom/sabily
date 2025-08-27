from django.conf import settings
from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Contribution(AllMixinInheritedMixin):
    class ContributionStatus(models.TextChoices):
        PENDING = "pending", "PENDING"
        CONFIRMED = "confirmed", "CONFIRMED"
        REJECTED = "rejected", "REJECTED"
        DELIVERED = "delivered", "DELIVERED"
        CANCELLED = "cancelled", "CANCELLED"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="user_%(class)s_set",
    )
    charity = models.ForeignKey(
        "Charity", on_delete=models.PROTECT, related_name="charity_%(class)s_set"
    )
    status = models.CharField(
        max_length=20,
        choices=ContributionStatus.choices,
        default=ContributionStatus.PENDING,
    )
    date_confirmed = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    receipt_sent = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-date_confirmed", "-updated_at"]
        indexes = [
            models.Index(
                fields=["user", "charity", "created_at"],
                name="user_charity_created_at_idx",
            ),
        ]

    def __str__(self):
        return f"{self.charity} - {self.user.get_full_name()}"
