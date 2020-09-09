from rest_framework import serializers
from .models import ad_type
from .models import feedback


class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        # fields = '__all__'
        fields = ['type_id', 'type_name']


class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'
