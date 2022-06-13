from django.db import models

class NewsPiece(models.Model):
    title = models.CharField(max_length=100)
    blurb = models.TextField()
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.title


