from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from .serializers import RegistrationSerializer, ChangePasswordSerializer, ProfileSerializer
from django.shortcuts import get_object_or_404
from ...models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ...models import Profile

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
        

class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset = None):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {'old_password': ['Wrong Password']},
                    status= status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(
                {'Detail': 'password changed successfully'},
                status = status.HTTP_200_OK
            )
        return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)



class ProfileApiView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset =  Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user = self.request.user.id)
        return obj