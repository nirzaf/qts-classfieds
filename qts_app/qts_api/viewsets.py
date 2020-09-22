from rest_framework import viewsets
from . import models, serailizers


class parent_categoryViewSet(viewsets.ModelViewSet):
    queryset = models.parent_category.objects.all()
    serializer_class = serailizers.parent_categorySerializer


class sub_categoryViewSet(viewsets.ModelViewSet):
    queryset = models.sub_category.objects.all()
    serializer_class = serailizers.sub_categorySerializer


class ad_listingViewSet(viewsets.ModelViewSet):
    queryset = models.ad_listing.objects.all()
    serializer_class = serailizers.ad_listingSerializer

    
class ad_typeViewSet(viewsets.ModelViewSet):
    queryset = models.ad_type.objects.all()
    serializer_class = serailizers.ad_typeSerializer


class feedbackViewSet(viewsets.ModelViewSet):
    queryset = models.feedback.objects.all()
    serializer_class = serailizers.feedbackSerializer


class districtViewSet(viewsets.ModelViewSet):
    queryset = models.district.objects.all()
    serializer_class = serailizers.districtSerializer


class cityViewSet(viewsets.ModelViewSet):
    queryset = models.city.objects.all()
    serializer_class = serailizers.citySerializer


class imageViewSet(viewsets.ModelViewSet):
    queryset = models.image.objects.all()
    serializer_class = serailizers.imageSeralizer

    
class userViewSet(viewsets.ModelViewSet):
    queryset = models.user.objects.all()
    serializer_class = serailizers.userSerializer


class promoted_ad_detailViewSet(viewsets.ModelViewSet):
    queryset = models.promoted_ad_detail.objects.all()
    serializer_class = serailizers.promoted_ad_detail


class promotion_packageViewSet(viewsets.ModelViewSet):
    queryset = models.promotion_package.objects.all()
    serializer_class = serailizers.promotion_packageSerializer


class paymentViewSet(viewsets.ModelViewSet):
    queryset = models.payment.objects.all()
    serializer_class = serailizers.paymentSerializer
