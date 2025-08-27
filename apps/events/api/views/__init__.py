from .tag_viewset import TagViewSet
from .event_viewset import EventViewSet
from .event_type_viewset import EventTypeViewSet
from .speaker_viewset import SpeakerViewSet
from .photo_viewset import PhotoViewSet
from .attendee_viewset import AttendeeViewSet
from .location_viewset import LocationViewSet
from .online_platform_viewset import OnlinePlatformViewSet
from .resource_viewset import ResourceViewSet
from .program_order_viewset import ProgramOrderViewSet


__all__ = [
    "EventViewSet",
    "EventTypeViewSet",
    "SpeakerViewSet",
    "PhotoViewSet",
    "AttendeeViewSet",
    "LocationViewSet",
    "ResourceViewSet",
    "ProgramOrderViewSet",
    "TagViewSet",
    "OnlinePlatformViewSet",
]
