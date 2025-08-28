from .tag_serializer import TagSerializer as TagSerializerV1
from .event_serializer import EventSerializer as EventSerializerV1
from .photo_serializer import PhotoSerializer as PhotoSerializerV1
from .speaker_serializer import SpeakerSerializer as SpeakerSerializerV1
from .attendee_serializer import AttendeeSerializer as AttendeeSerializerV1
from .location_serializer import LocationSerializer as LocationSerializerV1
from .event_type_serializer import EventTypeSerializer as EventTypeSerializerV1
from .resource_serializer import ResourceSerializer as ResourceSerializerV1
from .online_platform_serializer import (
    OnlinePlatformSerializer as OnlinePlatformSerializerV1,
)
from .program_order_serializer import ProgramOrderSerializer as ProgramOrderSerializerV1


__all__ = [
    "TagSerializerV1",
    "EventSerializerV1",
    "PhotoSerializerV1",
    "SpeakerSerializerV1",
    "AttendeeSerializerV1",
    "LocationSerializerV1",
    "EventTypeSerializerV1",
    "ResourceSerializerV1",
    "OnlinePlatformSerializerV1",
    "ProgramOrderSerializerV1",
]
