from django.db import models
class Adtypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)
    Is_deleted = models.BooleanField(default=True)