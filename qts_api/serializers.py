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


class ad_typeSerializer(serializers.Serializer):
    type_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return ad_type.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.type_name = validated_data.get('type_name', instance.type_name)
        instance.save()
        return instance
