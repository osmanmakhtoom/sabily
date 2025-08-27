from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib.contenttypes.admin import GenericStackedInline

from apps.charity.models import (
    CashContribution,
    GoodsContribution,
    ServiceContribution,
    ContributionFulfillment,
    Charity,
    CharityNeed,
    CharityNeedMedia,
    CharityType,
    DonationItemType,
)
from utils.bases.base_admin import BaseAdmin


class ContributionFulfillmentInline(GenericStackedInline):
    model = ContributionFulfillment
    extra = 0
    fields = (
        "need",
        "quantity_applied",
        "notes",
        "verified_by",
        "verified_at",
        "is_verified",
    )
    readonly_fields = ("created_at", "updated_at")


class CharityNeedMediaInline(TabularInline):
    model = CharityNeedMedia
    extra = 0
    fields = (
        "image",
        "description",
        "verified_by",
        "verified_at",
        "is_verified",
    )

    readonly_fields = ("created_at", "updated_at")


@admin.register(CashContribution)
class CashContributionAdmin(BaseAdmin):
    inlines = [ContributionFulfillmentInline]


@admin.register(GoodsContribution)
class GoodsContributionAdmin(BaseAdmin):
    inlines = [ContributionFulfillmentInline]


@admin.register(ServiceContribution)
class ServiceContributionAdmin(BaseAdmin):
    inlines = [ContributionFulfillmentInline]


@admin.register(Charity)
class CharityAdmin(BaseAdmin):
    pass


@admin.register(CharityNeed)
class CharityNeedAdmin(BaseAdmin):
    inlines = [CharityNeedMediaInline]


@admin.register(CharityType)
class CharityTypeAdmin(BaseAdmin):
    pass


@admin.register(DonationItemType)
class DonationItemTypeAdmin(BaseAdmin):
    pass
