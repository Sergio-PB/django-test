from django.contrib import admin
from django.urls import path
from .views import basic_resp

urlpatterns = [
    path('', basic_resp),
]
