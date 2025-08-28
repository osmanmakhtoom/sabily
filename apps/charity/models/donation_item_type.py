from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class DonationItemType(AllMixinInheritedMixin):
    class Category(models.TextChoices):
        CASH = "cash", "CASH"
        GOODS = "goods", "GOODS"
        SERVICES = "services", "SERVICES"
        OTHER = "other", "OTHER"

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.CASH
    )
    unit = models.CharField(max_length=20, blank=True)  # kg, pieces, hours, etc.
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to="donation_types_icons/", blank=True)
    is_acceptable = models.BooleanField(default=False)

    class Meta:
        unique_together = [["name", "category"]]
        ordering = ["id", "category", "name", "-created_at", "-updated_at"]

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"
