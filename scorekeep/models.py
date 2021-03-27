from django.db import models
from .choices import sport_choices

# Create your models here.
class ScoreCreate(models.Model):
    title = models.CharField(max_length=120, blank=False)
    slug = models.SlugField(unique=True, default=1, null=True)
    sport = models.CharField(max_length=2, choices=sport_choices, default='VB',)
    home = models.CharField(max_length=120, blank=False)
    away = models.CharField(max_length=120, blank=False)
    date = models.DateField(blank=False)
    startTime = models.TimeField(blank=False)
    homeScore = models.IntegerField(default=0, null=True)
    awayScore = models.IntegerField(default=0, null=True)

    objects = models.Manager()

    def get_absolute_url(self):
        if self.sport == "VB":
            return f"/score/vbscore/{self.slug}"
        elif self.sport == "BB":
            return f"/score/bbscore/{self.slug}"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"