from rest_framework import serializers

from .models import ad_type, payment, ad_listing, promotion_package, feedback, sub_category
from .models import district

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



