from django.db import models


class Video(models.Model):

    movie = models.FileField(upload_to='movies/')
    summary = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.summary
