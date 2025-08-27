from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class ProgramOrder(AllMixinInheritedMixin):
    event = models.ForeignKey(
        "Event", on_delete=models.CASCADE, related_name="programs"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    speakers = models.ManyToManyField("Speaker", blank=True)
    location = models.ForeignKey(
        "Location", on_delete=models.SET_NULL, null=True, blank=True
    )
    online_details = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "start_time"]

    def __str__(self):
        return f"{self.title} @ {self.event}"
