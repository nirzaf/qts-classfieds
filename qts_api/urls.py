from django.urls import path
from .views import GenericAdTypeAPI, GenericAdTypeGetAPI

urlpatterns = [
    path('api/ad_types', GenericAdTypeGetAPI.as_view()),
    path('api/ad_types/<int:pk>/', GenericAdTypeAPI.as_view())
]
