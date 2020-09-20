from rest_framework import serializers
from .models import promoted_ad_detail

class promoted_ad_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = promoted_ad_detail
        fields = '__all__'