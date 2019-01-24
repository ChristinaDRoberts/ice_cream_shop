from django.db import models

# Create your models here.
class IceCream(models.Model):
    flavor = models.CharField(max_length = 50)
    base =  models.CharField(max_length = 50)
    available = models.CharField(max_length = 50)
    featured = models.BooleanField
    date_churned = models.DateField

    def __str__(self):
        return self.name