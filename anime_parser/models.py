from django.db import models

class Anime(models.Model):
    title = models.CharField(null=True)
    year = models.IntegerField(max_length=10)
    city = models.CharField(max_length=20)
    genre = models.CharField(max_length=30)
    link = models.CharField(max_length=255)

    class Meta:
       verbose_name = "Список аниме"
       verbose_name = "Аниме"