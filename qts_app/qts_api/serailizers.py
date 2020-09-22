from rest_framework import serializers
from .models import ad_type
from .models import payment
from .models import ad_listing
from .models import promotion_package
from .models import feedback
from .models import user
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


class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = district
        fields = '__all__'


class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '___all_'


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'


class ad_listingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_listing
        fields = '__all__'


class ad_listingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_listing
        fields = '__all__'


class promotion_packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = promotion_package
        fields = '__all__'
