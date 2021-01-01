from django.db import models


class NewsType(models.Model):
    tName = models.CharField(max_length=50, unique=False)


class NewsInfo(models.Model):
    nTitle = models.CharField(max_length=100, null=True)
    nAuthor = models.CharField(max_length=20, null=True)
    nContent = models.CharField(max_length=1000, null=True)
    nPubDateTime = models.DateTimeField(auto_now_add=True)
    nStatus = models.IntegerField()
    tid = models.ForeignKey(NewsType, on_delete=models.CASCADE)
