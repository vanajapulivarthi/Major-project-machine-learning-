
from django.urls import path
from .views import Home,result

urlpatterns = [
    path('',Home),
    path('result/',result),
]
