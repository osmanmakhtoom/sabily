from django.contrib import admin
from apps.events.models import (
    EventType,
    Event,
    Tag,
    Speaker,
    Resource,
    Photo,
    ProgramOrder,
    Location,
    OnlinePlatform,
    Attendee,
)
from utils.bases.base_admin import BaseAdmin


class TagInline(admin.TabularInline):
    model = Event.tags.through
    extra = 1
    verbose_name_plural = "Tags"


class SpeakerInline(admin.TabularInline):
    model = Event.speakers.through
    extra = 1


class ResourceInline(admin.StackedInline):
    model = Resource
    extra = 1


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class ProgramOrderInline(admin.StackedInline):
    model = ProgramOrder
    extra = 1
    ordering = ("order",)


class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 0
    readonly_fields = ("created_at",)


@admin.register(Event)
class EventAdmin(BaseAdmin):
    inlines = [
        TagInline,
        SpeakerInline,
        ResourceInline,
        PhotoInline,
        ProgramOrderInline,
        AttendeeInline,
    ]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "description",
                    "event_type",
                    "tags",
                    "speakers",
                    "mode",
                )
            },
        ),
        (
            "Timing",
            {"fields": ("event_start", "event_end", "registration_deadline")},
        ),
        ("Location", {"fields": ("location", "online_platform", "meeting_url")}),
        (
            "Details",
            {
                "fields": (
                    "image",
                    "is_free",
                    "price",
                    "capacity",
                    "registration_required",
                )
            },
        ),
    )

    list_display = ("title", "event_type", "event_start", "location", "is_active")
    list_filter = ("event_type", "is_active", "event_start")
    search_fields = ("title", "description")
    filter_horizontal = ("tags", "speakers")

    autocomplete_fields = ["location", "online_platform"]
    raw_id_fields = ["event_type"]


@admin.register(EventType)
class EventTypeAdmin(BaseAdmin):
    search_fields = ("name",)


@admin.register(Location)
class LocationAdmin(BaseAdmin):
    list_display = ("name", "city", "country")
    search_fields = ("name", "city", "country")


@admin.register(OnlinePlatform)
class OnlinePlatformAdmin(BaseAdmin):
    list_display = ("name", "website")
    search_fields = ("name",)


@admin.register(Speaker)
class SpeakerAdmin(BaseAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(BaseAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
