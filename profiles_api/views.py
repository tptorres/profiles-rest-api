from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # list of HTTP status codes to use in the API
from . import serializers


class HelloApiView(APIView):
    """Test API View"""

    # whenever you're sending a post, put, or path request, expect an input with name and we're gonna validate it with this serializer
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as functions(get, post, patch, put, delete",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped maunally to URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                # dff
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})

