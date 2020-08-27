from django.db import models

# Create your models here.
class Ad(models.Model):
    ad_id = models.AutoField(unique=True, blank=False)
    ad_name = models.CharField(max_length=50, null=False)
    ad_type = models.ForeignKey(ad_type, on_delete=models.CASCADE, null=False)
    ad_price = models.FloatField(default=0, null=False, blank=False)
    ad_status = models.CharField(max_length=20, null=True)
    ad_category = models.ForeignKey(sub_category, on_delete=models.CASCADE, null=False)
    city_id = models.ForeignKey(district, on_delete=models.CASCADE, null=False)
    ad_duration = models.IntegerField(null=False)
    ad_is_promoted = models.BooleanField(null=False)
    promotion_duration = models.IntegerField(null=False)
    ad_posted_by = models.ForeignKey(user, on_delete=models.CASCADE, null=False)
    ad_posted_date = models.DateField(auto_now=True, auto_now_add=True, null=False)
    Is_deleted = models.BooleanField(default=False, null=False)
