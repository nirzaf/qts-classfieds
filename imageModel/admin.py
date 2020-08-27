from django.contrib import admin

from .models import image
from .models import ad

admin.site.register(ad)
admin.site.register(image)
