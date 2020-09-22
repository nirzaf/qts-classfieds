from rest_framework import serializers
from .models import feedback
from .models import user
from .models import district
from .models import image
from .models import sub_category
from .models import parent_category
from .models import promoted_ad_detail
from .models import city
from .models import ad_listing
from .models import payment
from .models import ad_type
from .models import promotion_package


class parent_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = parent_category
        fields = '__all__'


class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = '__all__'


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


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = district
        fields = '__all__'


class imageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '___all__'


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


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'


class promoted_ad_detail(serializers.ModelSerializer):
    class Meta:
        model = promoted_ad_detail
        fields = '__all__'
