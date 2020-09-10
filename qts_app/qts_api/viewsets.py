from rest_framework import viewsets
from . import models
from . import serailizers

class ad_listingViewSet(viewsets.ModelViewSet):
    queryset = models.ad_listing.objects.all()
    serializer_class = serailizers.ad_listingSerializer


class ad_typeViewSet(viewsets.ModelViewSet):
    queryset = models.ad_type.objects.all()
    serializer_class = serailizers.ad_typeSerializer


