from rest_framework import serializers
from .models import ad_type, payment, ad_listing, promotion_package, feedback
from .models import district


class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        fields = '__all__'


class promotion_packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = promotion_package
        fields = '__all__'
        
        
class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'

class ad_listingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_listing
        fields = '__all__'

#District serializer
class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = district
        fields = '__all__'
