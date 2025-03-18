from . import views
from django.urls import path

urlpatterns = [path("", views.HelloWorld, name="HelloWorld")]
