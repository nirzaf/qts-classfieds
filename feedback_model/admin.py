from django.contrib import admin
from .models import User, Feedback

# Register your models here.
admin.site.register(User)
admin.site.register(Feedback)