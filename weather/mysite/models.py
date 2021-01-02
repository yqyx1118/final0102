from django.db import models

class Taiwan(models.Model):
    city = models.CharField(max_length=200)
    def __str__(self):
        return self.city
    

# Create your models here.
