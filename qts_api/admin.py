from django.contrib import admin
from .models import ad_type
from .models import ad_listing
from .models import image
from .models import promotion_package
from .models import promoted_ad_detail
from .models import parent_category
from .models import payment
from .models import city
from .models import district
from .models import feedback
from .models import sub_category
from .models import user

# Register your models here.
admin.site.register(ad_type)
admin.site.register(ad_listing)
admin.site.register(image)
admin.site.register(promotion_package)
admin.site.register(promoted_ad_detail)
admin.site.register(parent_category)
admin.site.register(payment)
admin.site.register(city)
admin.site.register(sub_category)
admin.site.register(user)
admin.site.register(district)
admin.site.register(feedback)

