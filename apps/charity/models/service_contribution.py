from django.db import models

from apps.charity.models.contribution import Contribution


class ServiceContribution(Contribution):
    service_type = models.ForeignKey(
        "DonationItemType",
        on_delete=models.PROTECT,
        limit_choices_to={"category": "services"},
    )
    hours_contributed = models.PositiveIntegerField()
    estimated_value = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = [
            "service_type",
            "hours_contributed",
            "estimated_value",
            "-created_at",
        ]
