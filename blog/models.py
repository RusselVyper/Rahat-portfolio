from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=500, null=True)
    pub_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
