from django.db import models

class ConvertedUrls(models.Model):
    url = models.URLField(max_length=250)

    def __str__(self):
        return self.url