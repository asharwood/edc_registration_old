from django.db import models

TITLE_CHOICES = (
              ("", ""),
              ("Mr","Mr"),
              ("Mrs","Mrs"),
              ("Dr","Dr"),
              ("Miss","Miss"),
              ("Ms","Ms"),
              ("Prof","Prof")
          )

class Dataset (models.Model):
   name = models.CharField(max_length=100)

   def __unicode__(self):
        return self.name

class Condition (models.Model):
   dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
   version = models.IntegerField()   
   text    = models.CharField(max_length=10000)
   comment = models.CharField(max_length=500, blank=True)

class User (models.Model):

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)

    firstName    = models.CharField(max_length=50)
    lastName     = models.CharField(max_length=50)
    emailaddress = models.CharField(max_length=50)
    department   = models.CharField(max_length=100)
    institute    = models.CharField(max_length=100)
    dataUse      = models.CharField(max_length=1500)
    startdate    = models.DateTimeField()    
    condition    = models.ForeignKey(Condition, on_delete=models.CASCADE)

