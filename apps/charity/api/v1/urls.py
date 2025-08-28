from rest_framework import routers

from apps.charity.api.views import (
    CharityTypeViewSet,
    CharityViewSet,
    CharityNeedViewSet,
    DonationItemTypeViewSet,
    CashContributionViewSet,
    GoodsContributionViewSet,
    ServiceContributionViewSet,
    ContributionFulfillmentViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)

router.register(r"charity-types", CharityTypeViewSet, basename="charity-types")
router.register(r"charities", CharityViewSet, basename="charities")
router.register(r"charity-needs", CharityNeedViewSet, basename="charity-needs")
router.register(
    r"donation-item-types", DonationItemTypeViewSet, basename="donation-item-types"
)
router.register(
    r"cash-contributions", CashContributionViewSet, basename="cash-contributions"
)
router.register(
    r"goods-contributions", GoodsContributionViewSet, basename="goods-contributions"
)
router.register(
    r"service-contributions",
    ServiceContributionViewSet,
    basename="service-contributions",
)
router.register(
    r"contributions", ContributionFulfillmentViewSet, basename="contributions"
)

urlpatterns = router.urls
