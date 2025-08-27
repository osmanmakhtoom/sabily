from django.conf import settings
from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Attendee(AllMixinInheritedMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="event_registrations",
    )
    event = models.ForeignKey(
        "Event", on_delete=models.CASCADE, related_name="attendees"
    )
    attended = models.BooleanField(default=False)
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user} registered for {self.event}"
