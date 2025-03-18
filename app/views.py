from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class HelloWorldClass(APIView):
    def get(self, request):
        resp = {
            "status": "Success",
            "Message": "Welcome to Our Page",
            "Content": "Loading...",
        }
        return Response(resp)


HelloWorld = HelloWorldClass.as_view()
