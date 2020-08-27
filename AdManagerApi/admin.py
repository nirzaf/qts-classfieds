from django.contrib import admin

from .models import promotion_ad_details
from .models import ad
from .models import promotion_package

admin.site.register(ad)
admin.site.register(promotion_package)
admin.site.register(promotion_ad_details)