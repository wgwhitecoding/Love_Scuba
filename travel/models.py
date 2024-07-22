from django.db import models

class DiveLocation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    best_season = models.CharField(max_length=255)
    image = models.ImageField(upload_to='travel_images/', blank=True)

    def __str__(self):
        return self.name
