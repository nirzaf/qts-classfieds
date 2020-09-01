from django.http import JsonResponse
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import ad_type
from .serializers import ad_typeSerializer

from .models import ad_listing
from .models import image
from .models import promotion_package
from .models import promoted_ad_detail
from .models import parent_category
from .models import payment
from .models import city
from .models import district
from .models import feedback
from .models import sub_category
from .models import user

from .serializers import ad_typeSerializer


# Create your views here.

class GenericAdTypeAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin):
    serializer_class = ad_typeSerializer
    queryset = ad_type.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request, pk=pk)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)


class GenericAdTypeGetAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ad_type
    queryset = ad_type.objects.all()

    def get(self, request):
        return self.list(request)
