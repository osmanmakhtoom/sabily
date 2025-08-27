from django.db import models

from utils.model_mixins import AllMixinInheritedMixin


class Surah(AllMixinInheritedMixin):
    class RELEVATION(models.TextChoices):
        MAKKY = "MAKKI", "Makki"
        MADANI = "MADANI", "Madani"

    number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    name_english = models.CharField(max_length=50)
    name_arabic = models.CharField(max_length=50)
    revelation_type = models.CharField(
        max_length=10, choices=RELEVATION.choices, default=RELEVATION.MAKKY
    )
    total_ayahs = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Suwar"

    def __str__(self):
        return f"{self.number}. {self.name} ({self.name_english})"


class Ayah(AllMixinInheritedMixin):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE, related_name="ayahs")
    number = models.PositiveSmallIntegerField()
    text = models.TextField()
    text_clean = models.TextField(help_text="Text without diacritics for search")
    tajweed_rules = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["surah__number", "number"]
        unique_together = ("surah", "number")
        verbose_name_plural = "Ayahs"

    def __str__(self):
        return f"{self.surah.number}:{self.number}"


class TafseerSource(AllMixinInheritedMixin):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    source_url = models.URLField(blank=True)
    published_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Tafseer Source"
        verbose_name_plural = "Tafseer Sources"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} by {self.author}"


class AyahTafseer(AllMixinInheritedMixin):
    ayah = models.ForeignKey("Ayah", on_delete=models.CASCADE, related_name="tafseers")
    source = models.ForeignKey(TafseerSource, on_delete=models.CASCADE)
    text = models.TextField()
    additional_notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Ayah Tafseer"
        verbose_name_plural = "Ayah Tafaseer"
        unique_together = ("ayah", "source")
        ordering = ["ayah__surah__number", "ayah__number"]

    def __str__(self):
        return f"Tafseer of {self.ayah} from {self.source}"


class SurahTafseer(AllMixinInheritedMixin):
    surah = models.ForeignKey(
        "Surah", on_delete=models.CASCADE, related_name="tafseers"
    )
    source = models.ForeignKey(TafseerSource, on_delete=models.CASCADE)
    introduction = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    lessons = models.TextField(blank=True)

    class Meta:
        verbose_name = "Surah Tafseer"
        verbose_name_plural = "Surah Tafaseer"
        unique_together = ("surah", "source")
        ordering = ["surah__number"]

    def __str__(self):
        return f"Tafseer of {self.surah} from {self.source}"


class Reciter(AllMixinInheritedMixin):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="reciters/", blank=True)
    style = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    death_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class RecitationType(AllMixinInheritedMixin):
    name = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    riwaya = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.riwaya})" if self.riwaya else self.name


class AyahAudio(AllMixinInheritedMixin):
    ayah = models.ForeignKey("Ayah", on_delete=models.CASCADE, related_name="audios")
    reciter = models.ForeignKey(Reciter, on_delete=models.CASCADE)
    recitation_type = models.ForeignKey(
        RecitationType, on_delete=models.SET_NULL, null=True, blank=True
    )
    audio_file = models.FileField(upload_to="quran/audio/ayahs/")
    duration = models.DurationField(null=True, blank=True)
    bitrate = models.PositiveIntegerField(null=True, blank=True, help_text="In kbps")

    class Meta:
        verbose_name = "Ayah Audio"
        verbose_name_plural = "Ayah Audios"
        unique_together = ("ayah", "reciter", "recitation_type")
        ordering = ["ayah__surah__number", "ayah__number"]

    def __str__(self):
        return f"Audio of {self.ayah} by {self.reciter}"


class SurahAudio(AllMixinInheritedMixin):
    surah = models.ForeignKey("Surah", on_delete=models.CASCADE, related_name="audios")
    reciter = models.ForeignKey(Reciter, on_delete=models.CASCADE)
    recitation_type = models.ForeignKey(
        RecitationType, on_delete=models.SET_NULL, null=True, blank=True
    )
    audio_file = models.FileField(upload_to="quran/audio/surahs/")
    duration = models.DurationField(null=True, blank=True)
    bitrate = models.PositiveIntegerField(null=True, blank=True, help_text="In kbps")

    class Meta:
        verbose_name = "Surah Audio"
        verbose_name_plural = "Surah Audios"
        unique_together = ("surah", "reciter", "recitation_type")
        ordering = ["surah__number"]

    def __str__(self):
        return f"Audio of {self.surah} by {self.reciter}"
