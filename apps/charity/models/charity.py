from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Charity(AllMixinInheritedMixin):
    name = models.CharField(max_length=200)
    description = models.TextField()
    charity_types = models.ManyToManyField("CharityType")
    accepts_donation_types = models.ManyToManyField("DonationItemType")
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="charity_logos/", blank=True)
    established_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["id", "name", "-established_date"]

    def __str__(self):
        return f"{self.name}"

    @property
    def current_needs(self):
        return self.needs.filter(is_active=True, remaining_quantity__gt=0)
