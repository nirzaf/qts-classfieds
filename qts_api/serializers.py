from rest_framework import serializers
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


class ad_typeSerializer(serializers.ModelSerializers):
    class Meta:
        model = ad_type
        fields = ['type_id', 'type_name']


