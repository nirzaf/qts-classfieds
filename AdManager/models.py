from django.db import models


# Create your models here.
class promotion_packages(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    promotion_name = models.CharField(max_length=30)
    promotion_cost = models.FloatField()
    duration = models.IntegerField()
    is_deleted = models.BooleanField()

    def __str__(self):
        return self.promotion_id
