from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ad_type(models.Model):
    type_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    type_name = models.CharField(max_length=50)
    Is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Ad Type with Id :" + str(self.type_id) + " is added!"


class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    json_token = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "User with Id :" + str(self.user_id) + " is added!"


class parent_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Parent Category with Id :" + str(self.user_id) + " is added!"


class sub_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=120)
    parent_category = models.ForeignKey(parent_category, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "sub_category with Id :" + str(self.category_id) + " is added!"


class district(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=100)

    def __str__(self):
        return "District with Id :" + str(self.district_id) + " is added!"


class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=70)
    district_id = models.ForeignKey(district, on_delete=models.CASCADE)

    def __str__(self):
        return "City with Id :" + str(self.city_id) + " is added!"

class ad_listing(models.Model):
    ad_id = models.BigAutoField(primary_key=True)
    ad_name = models.CharField(max_length=150)
    ad_type = models.ForeignKey(ad_type, on_delete=models.CASCADE)
    ad_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ad_status = models.IntegerField()
    ad_duration = models.IntegerField
    is_ad_promoted = models.BooleanField(default=False)
    promotion_duration = models.IntegerField()
    ad_posted_date = models.DateField
    ad_posted_by = models.ForeignKey(user, on_delete=models.CASCADE)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    ad_category = models.ForeignKey(sub_category, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Ad Listing with Id :" + str(self.ad_id) + " is added!"


class image(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(ad_listing, on_delete=models.CASCADE)
    url = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "District with Id :" + str(self.image_id) + " is added!"


class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    rating = models.IntegerField(default=1)
    comments = models.TextField(max_length=250)
    user_id = models.IntegerField()
    commented_user = models.ForeignKey(user, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Feedback with Id :" + str(self.feedback_id) + " is added!"


class promotion_package(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    promotion_name = models.CharField(max_length=150)
    promotion_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    duration = models.IntegerField
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Promotion Package with Id :" + str(self.promotion_id) + " is added!"


class promoted_ad_detail(models.Model):
    pa_ad_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(ad_listing, on_delete=models.CASCADE)
    starting_date = models.DateField
    status = models.IntegerField
    promotion_id = models.ForeignKey(promotion_package, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(primary_key=False)

    def __str__(self):
        return "District with Id :" + str(self.pa_ad_id) + " is added!"


class payment(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    promoted_ad_id = models.ForeignKey(promoted_ad_detail, on_delete=models.CASCADE)
    payment_date = models.DateField
    payment_time = models.TimeField
    paid_amount = models.DecimalField
    payment_status = models.BooleanField(default=True)

    def __str__(self):
        return "District with Id :" + str(self.payment_id) + " is added!"


