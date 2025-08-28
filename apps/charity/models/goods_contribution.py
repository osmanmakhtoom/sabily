from django.db import models

from apps.charity.models.contribution import Contribution


class GoodsContribution(Contribution):
    class DeliveryMethod(models.TextChoices):
        DROP_OFF = "drop_off", "DROP OFF"
        PICK_UP = "pick_up", "PICK UP"
        SHIPPED = "shipped", "SHIPPED"

    item_type = models.ForeignKey(
        "DonationItemType",
        on_delete=models.PROTECT,
        limit_choices_to={"category": "goods"},
    )
    quantity = models.PositiveIntegerField()
    estimated_value = models.PositiveIntegerField(null=True, blank=True)
    delivery_method = models.CharField(
        max_length=50,
        choices=DeliveryMethod.choices,
        default=DeliveryMethod.DROP_OFF,
    )
    tracking_number = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = (
            "id",
            "quantity",
            "-created_at",
        )
