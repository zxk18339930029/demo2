from django.db import models


class Like(model.Models):
    uid = models.IntegerField()
    name = models.CharField()

# Create your models here.
