from rest_framework import viewsets
from . import models, serailizers

class ad_listingViewSet(viewsets.ModelViewSet):
    queryset = models.ad_listing.objects.all()
    serializer_class = serailizers.ad_listingSerializer


class ad_typeViewSet(viewsets.ModelViewSet):
    queryset = models.ad_type.objects.all()
    serializer_class = serailizers.ad_typeSerializer


class promotion_packageViewSet(viewsets.ModelViewSet):
    queryset = models.promotion_package.objects.all()
    serializer_class = serailizers.promotion_packageSerializer

    
class feedbackViewSet(viewsets.ModelViewSet):
    queryset = models.feedback.objects.all()
    serializer_class = serailizers.feedbackSerializer


class districtViewSet(viewsets.ModelViewSet):
    queryset = models.district.objects.all()
    serializer_class = serailizers.districtSerializer


class imageViewSet(viewsets.ModelViewSet):
    queryset = models.image.objects.all()
    serializer_class = serailizers.imageSeralizer