from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class ad(models.Model):
    ad_id=models.IntegerField(primary_key=True)

class image(models.Model):
    image_id=models.IntegerField(primary_key=True)
    ad_id=models.ForeignKey(ad,on_delete=models.CASCADE,default=None)
    url=models.CharField(max_length=100,default=None)
    is_deleted = models.BooleanField(default=False)

