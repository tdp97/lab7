from django.db import models


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125)




