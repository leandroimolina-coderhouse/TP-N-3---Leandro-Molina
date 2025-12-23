from django.urls import path
from hospital.views import *

urlpatterns = [
    path("",home, name="home"),
]