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


HelloWorld = hello_world_class.as_view()
