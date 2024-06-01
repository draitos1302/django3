from django.urls import path
from django.urls import include
from .views import homepageview

urlpatterns = [

    path("",homepageview.as_view(), name = "home"),

]