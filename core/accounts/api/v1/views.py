from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer
from django.shortcuts import get_object_or_404
from ...models import User
from rest_framework.response import Response
from rest_framework import status

class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
            }
            return Response(data, status= status.HTTP_201_CREATED)
