from . import tasks
from . import serializers
from . import models

from .permission import IsOwnerOrReadeOnly

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from redis import Redis
from django.utils.crypto import get_random_string


con = Redis(host="localhost", port=6381, db=0, charset="utf-8", decode_responses=True)


class UserLogin(APIView):
    """
    Clients can use this APIView to receive an OTP for login/register.
    """
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get("phone_number")
        otp_cachee = con.get(phone_number)
        if otp_cachee is None:
            tasks.send_sms(phone_number)
            return Response("code sends to your phone", status=status.HTTP_200_OK)
        else:
            return Response(f"your code was: {otp_cachee}", status=status.HTTP_200_OK)
        
        
class UserVerify(APIView):
    """
    No matter clients are going to login or register, they can call this api
    to verify their OTPs and receive access & refresh token for further uses.
    """
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserVeifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get("phone_number")
        otp_cache = con.get(phone_number)
        otp_user = serializer.validated_data.get("otp")
        
        if not otp_cache == otp_user:
            return Response("your code is not correct", status=status.HTTP_404_NOT_FOUND)
        
        obj, created = models.User.objects.get_or_create(username=phone_number, password=get_random_string(length=50))
        refresh_token = RefreshToken().for_user(obj)
        access_token = refresh_token.access_token
        return Response(
            data =
            {
            "id": obj.id ,
            "access_token" : str(access_token),
            "refresh_token": str(refresh_token),
            "created" : created
            }, status=status.HTTP_201_CREATED
        )


class PostCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = serializers.PostCrudSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        text = serializer.validated_data['text']
        queryset = models.PostCrud.objects.create(text=text, title=title, owner=request.user)
        response_data = {
            "id": queryset.id,
            "user": queryset.owner.username,
            "title": queryset.title,
            "text": queryset.text,
            "created_at": queryset.created_at,
            "modified_at": queryset.modified_at,
        }
        return Response(response_data, status=status.HTTP_200_OK)


class PostRetrieve(APIView):

    def get(self, request, pk):
        try:
            queryset = models.PostCrud.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        response_data = {
            "user": queryset.owner.username,
            "title": queryset.title,
            "text": queryset.text,
            "created": queryset.created_at,
            "modified": queryset.modified_at,
        }
        return Response(response_data, status=status.HTTP_200_OK)


class PostUpdate(APIView):
    permission_classes = [IsOwnerOrReadeOnly]
    
    def patch(self, request, pk):
        queryset = models.PostCrud.objects.get(pk=pk)
        self.check_object_permissions(request, queryset)
        serializer = serializers.PostCrudSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PostDelete(APIView):
    permission_classes = [IsOwnerOrReadeOnly]

    def delete(self, request, pk):
        queryset = models.PostCrud.objects.get(pk=pk)
        self.check_object_permissions(request, queryset)
        queryset.delete()
        return Response({'deleted'}, status=status.HTTP_200_OK)
