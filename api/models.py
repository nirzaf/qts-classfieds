from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Adtypes(models.Model):
    type_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    type_name = models.CharField(max_length=50)
    Is_deleted = models.BooleanField()
