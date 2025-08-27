from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Location(AllMixinInheritedMixin):
    name = models.CharField(max_length=255, db_index=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
