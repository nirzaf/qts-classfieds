from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Model Classes
class ad_types(models.Model):
    type_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    type_name = models.CharField(max_length=50)
    Is_deleted = models.BooleanField()


class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.TextField
    contact = models.CharField(max_length=20)
    user_type = models.IntegerField
    json_token = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)


class parent_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)


class sub_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=120)
    parent_category = models.ForeignKey(parent_category, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


class districts(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=100)


class cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=70)
    district_id = models.ForeignKey(districts, on_delete=models.CASCADE)


class ad_listing(models.Model):
    ad_id = models.BigAutoField(primary_key=True)
    ad_name = models.CharField(max_length=150)
    ad_type = models.ForeignKey(ad_types, on_delete=models.CASCADE)
    ad_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ad_status = models.IntegerField
    ad_duration = models.IntegerField
    is_ad_promoted = models.BooleanField(default=False)
    promotion_duration = models.IntegerField
    ad_posted_date = models.DateField
    ad_posted_by = models.ForeignKey(users, on_delete=models.CASCADE)
    city = models.ForeignKey(cities, on_delete=models.CASCADE)
    ad_category = models.ForeignKey(sub_category, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


class image(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(ad_listing, on_delete=models.CASCADE)
    url = models.TextField
    is_deleted = models.BooleanField(default=False)


class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    rating = models.IntegerField
    comments = models.TextField
    user_id = models.IntegerField
    commented_user = models.ForeignKey(users, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


class promotion_package(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    promotion_name = models.CharField(max_length=150)
    promotion_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    duration = models.IntegerField
    is_deleted = models.BooleanField(default=False)


class promoted_ad_details(models.Model):
    pa_ad_id = models.BigAutoField(primary_key=True)
    ad_id = models.ForeignKey(ad_listing, on_delete=models.CASCADE)
    starting_date = models.DateField
    status = models.IntegerField
    promotion_id = models.ForeignKey(promotion_package, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(primary_key=False)


class payment(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    promoted_ad_id = models.ForeignKey(promoted_ad_details, on_delete=models.CASCADE)
    payment_date = models.DateField
    payment_time = models.TimeField
    paid_amount = models.DecimalField
    payment_status = models.BooleanField(default=True)






