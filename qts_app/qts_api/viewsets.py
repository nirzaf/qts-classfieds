from rest_framework import viewsets
from . import models, serailizers


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


class userViewSet(viewsets.ModelViewSet):
    queryset = models.user.objects.all()
    serializer_class = serailizers.user_typeSerializer
