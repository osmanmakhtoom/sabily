from django.core.validators import URLValidator
from django.db import models
from django.utils import timezone

from utils.model_mixins import AllMixinInheritedMixin


class Event(AllMixinInheritedMixin):
    class EventMode(models.TextChoices):
        ONLINE = ("online", "Online")
        OFFLINE = ("offline", "In-Person")
        HYBRID = ("hybrid", "Hybrid")

    class Recurrence(models.TextChoices):
        NONE = ("none", "No Recurrence")
        DAILY = ("daily", "Daily")
        WEEKLY = ("weekly", "Weekly")
        MONTHLY = ("monthly", "Monthly")
        YEARLY = ("yearly", "Yearly")

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    event_type = models.ForeignKey(
        "EventType", on_delete=models.CASCADE, related_name="events"
    )
    mode = models.CharField(
        max_length=10, choices=EventMode.choices, default=EventMode.ONLINE
    )
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    organizer = models.CharField(max_length=255)
    image = models.ImageField(upload_to="event_images/", blank=True)
    is_free = models.BooleanField(default=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    registration_required = models.BooleanField(default=False)
    registration_deadline = models.DateTimeField(null=True, blank=True)
    location = models.OneToOneField(
        "Location",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    online_platform = models.ForeignKey(
        "OnlinePlatform",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="events",
    )
    meeting_url = models.URLField(validators=[URLValidator()], blank=True, null=True)
    meeting_id = models.CharField(max_length=100, blank=True)
    meeting_password = models.CharField(max_length=100, blank=True)
    recurrence_pattern = models.CharField(
        max_length=20,
        choices=Recurrence.choices,
        default=Recurrence.NONE,
    )
    recurrence_end = models.DateField(null=True, blank=True)
    excluded_dates = models.JSONField(default=list, blank=True)
    speakers = models.ManyToManyField("Speaker", blank=True, related_name="events")
    tags = models.ManyToManyField("Tag", blank=True, related_name="events")

    class Meta:
        ordering = ["title", "-event_start", "-event_end", "-created_at", "-updated_at"]

    def __str__(self):
        return f"{self.title} ({self.get_mode_display()})"

    @property
    def is_upcoming(self):
        return self.event_start > timezone.now()

    def save(self, *args, **kwargs):
        if (
            self.mode == Event.EventMode.ONLINE or self.mode == Event.EventMode.HYBRID
        ) and not self.meeting_url:
            raise ValueError("Online or Hybrid meeting URL must be specified")
        if (
            self.mode == Event.EventMode.OFFLINE
            or self.mode == Event.EventMode.HYBRID
            and not self.location
        ):
            raise ValueError("Offline or Hybrid location must be specified")
        super(Event, self).save(*args, **kwargs)
