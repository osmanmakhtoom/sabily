from rest_framework import routers

from apps.events.api.views import (
    EventViewSet,
    EventTypeViewSet,
    LocationViewSet,
    OnlinePlatformViewSet,
    ProgramOrderViewSet,
    PhotoViewSet,
    SpeakerViewSet,
    TagViewSet,
    AttendeeViewSet,
    ResourceViewSet,
)


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"events", EventViewSet, basename="events")
router.register(r"event-types", EventTypeViewSet, basename="event_types")
router.register(r"locations", LocationViewSet, basename="locations")
router.register(r"photos", PhotoViewSet, basename="photos")
router.register(r"speakers", SpeakerViewSet, basename="speakers")
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"attendees", AttendeeViewSet, basename="attendees")
router.register(r"resources", ResourceViewSet, basename="resources")
router.register(r"program-orders", ProgramOrderViewSet, basename="program-orders")
router.register(r"online-platforms", OnlinePlatformViewSet, basename="online-platforms")

urlpatterns = router.urls
