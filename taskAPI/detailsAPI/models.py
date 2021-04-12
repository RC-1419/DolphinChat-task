from django.db import models

# Create your models here.

class detailsapi_datatable(models.Model):
    id = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Email = models.CharField(max_length=70)
    Address1 = models.CharField(max_length=40)
    Address2 = models.CharField(max_length=40)
    Address3 = models.CharField(max_length=40)
