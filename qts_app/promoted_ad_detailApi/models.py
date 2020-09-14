from django.db import models

class ad_listing(models.Model):
    ad_id = models.BigAutoField(primary_key=True)

class promotion_package(models.Model):
    promotion_id = models.AutoField(primary_key=True)

class promoted_ad_detail(models.Model):
    pa_ad_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(ad_listing, on_delete=models.CASCADE)
    starting_date = models.DateField(auto_now_add=True,null=True)
    status = models.IntegerField(default=None)
    promotion_id = models.ForeignKey(promotion_package, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(primary_key=False)

    def __str__(self):
        return "Promoted_Ad_Detail with Id :" + str(self.pa_ad_id) + " is added!"
