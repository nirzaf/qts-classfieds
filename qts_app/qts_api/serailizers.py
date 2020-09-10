from rest_framework import serializers
from .models import ad_type, ad_listing


class ad_listingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ad_listing


class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        # fields = '__all__'
        fields = ['type_id', 'type_name']
