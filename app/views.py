from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class hello_world_class(APIView):
    def get(self, request):
        resp = {
            "status": "Success",
            "Message": "Welcome to Our Page",
            "Content": "Loading...",
        }
        return Response(resp)


class Greet_class(APIView):
    def get(self, request):
        resp = {
            "status": "Success",
            "Message": "Good Morning",
        }
        return Response(resp)


Greet = Greet_class.as_view()
HelloWorld = hello_world_class.as_view()
