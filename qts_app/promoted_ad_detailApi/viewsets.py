from rest_framework import viewsets
from . import models
from . import serailizers
# Create your views here.
class promoted_ad_detailViewSet(viewsets.ModelViewSet):
    queryset = models.promoted_ad_detail.objects.all()
    serializer_class = serailizers.promoted_ad_detailSerializer