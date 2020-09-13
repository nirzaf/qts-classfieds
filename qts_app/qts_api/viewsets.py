from rest_framework import viewsets
from . import models
from . import serailizers


class ad_typeViewSet(viewsets.ModelViewSet):
    queryset = models.ad_type.objects.all()
    serializer_class = serailizers.ad_typeSerializer


class promotion_packageViewSet(viewsets.ModelViewSet):
    queryset = models.promotion_package.objects.all()
    serializer_class = serailizers.promotion_packageSerializer

    
class feedbackViewSet(viewsets.ModelViewSet):
    queryset = models.feedback.objects.all()
    serializer_class = serailizers.feedbackSerializer

