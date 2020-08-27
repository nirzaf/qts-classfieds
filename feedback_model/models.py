from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user_id

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key = True)
    rating = models.IntegerField()
    comments = models.TextField(max_length=256)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    commented_user = models.ManyToManyField(User, related_name='commented_user', blank=True)
    is_deleted = models.BooleanField(default=0)

    def __str__(self):
        return self.feedback_id