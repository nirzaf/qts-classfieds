from django.db import models

# Create your models here.
class cities(models.Model) :
    city_id = models.AutoField(primary_key = True)
    city_name = models.CharField(max_length=70)
    district_id = models.ForeignKey(district , on_delete=models.CASCADE)
    

