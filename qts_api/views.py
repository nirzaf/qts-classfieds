from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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


# Create your views here.
def ad_type_list(request):
    if request.method == 'GET':
        types = ad_type.objects.all()
        serializer = ad_typeSerializer(types, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = ad_typeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=404)
