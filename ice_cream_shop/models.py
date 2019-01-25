from django.db import models
import datetime

# Create your models here.
class IceCream(models.Model):
    flavor = models.CharField(max_length = 50)
    base =  models.CharField(max_length = 50)
    available = models.CharField(max_length = 50)
    featured = models.BooleanField(null=True)
    date_churned = models.DateField(null=True)


    def __str__(self):
        return self.flavor



#
#
# class Photo(models.Model):
#     title = models.CharField(max_length = 50)
#     Picture = models.URLField()

#








