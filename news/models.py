from django.db import models


class HeadlineBasket(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class NewsPiece(models.Model):
    title = models.CharField(max_length=100)
    blurb = models.TextField()
    source = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default="")
    date = models.CharField(max_length=100, default="")
    headline = models.ForeignKey(HeadlineBasket, on_delete=models.CASCADE,default='')


    def __str__(self):
        return self.title





