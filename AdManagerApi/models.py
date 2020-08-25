from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class ad(models.Model):
    ad_id=models.IntegerField(primary_key=True)
class promotion_package(models.Model):
    promotion_id=models.IntegerField(primary_key=True)
class promotion_ad_details(models.Model):
    pa_ad_id=models.IntegerField(primary_key=True)
    ad_id=models.ForeignKey(ad,on_delete=models.CASCADE,default=None)
    promotion_id=models.ForeignKey(promotion_package,on_delete=models.CASCADE,default=None)
    status=models.IntegerField(validators=[MinValueValidator(0)],null=True)
    starting_date=models.DateField(null=True)
    is_deleted = models.BooleanField(default=False)

