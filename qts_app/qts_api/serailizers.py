from rest_framework import serializers
from .models import ad_type
from .models import promotion_package


class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        # fields = '__all__'
        fields = ['type_id', 'type_name']


class promotion_packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = promotion_package
        fields = '__all__'
