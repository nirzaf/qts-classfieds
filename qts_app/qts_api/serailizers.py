from rest_framework import serializers
from .models import ad_type, payment, ad_listing, promotion_package, feedback
from .models import district, image
from .models import sub_category

class sub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = sub_category
        fields = '__all__'


class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        fields = '__all__'


class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'


class user_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

        
#District serializer
class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = district
        fields = '__all__'


class imageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '___all_'

