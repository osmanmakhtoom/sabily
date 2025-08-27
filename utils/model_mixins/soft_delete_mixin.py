from django.db import models
from django.utils import timezone


class SoftDeleteMixin(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=True)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def soft_undelete(self):
        self.deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
