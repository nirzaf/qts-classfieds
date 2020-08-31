from django.contrib import admin
from django.urls import path, include
from .views import ad_type_list

urlpatterns = [
    path('admin/', admin.site.urls),
]
