from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class CharityNeed(AllMixinInheritedMixin):
    class Urgency(models.IntegerChoices):
        CRITICAL = 1, "CRITICAL"
        HIGH = 2, "HIGH"
        MEDIUM = 3, "MEDIUM"
        LOW = 4, "LOW"

    charity = models.ForeignKey(
        "Charity", on_delete=models.CASCADE, related_name="needs"
    )
    item_type = models.ForeignKey(
        "DonationItemType",
        on_delete=models.PROTECT,
        related_name="needs",
    )
    quantity_needed = models.PositiveIntegerField(null=True, blank=True)
    current_quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    urgency = models.PositiveSmallIntegerField(
        default=Urgency.MEDIUM, choices=Urgency.choices
    )

    class Meta:
        ordering = ["urgency", "-created_at", "-updated_at"]

    def __str__(self):
        return f"{self.charity.name} needs {self.item_type.name}"

    @property
    def remaining_quantity(self):
        return self.quantity_needed - self.fulfilled_quantity

    @property
    def fulfillment_percentage(self):
        if not self.quantity_needed:
            return 0
        return (self.fulfilled_quantity / self.quantity_needed) * 100

    @property
    def fulfilled_quantity(self):
        return sum(
            fulfillment.quantity_applied for fulfillment in self.fulfillments.all()
        )

    @property
    def images(self):
        return self.media.filter(is_active=True, is_verified=True)
