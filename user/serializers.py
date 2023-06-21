from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from . import models


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)

    def validate_phone_number(self, value):
        if not (value.startswith('09') and value.isnumeric() and len(value)==11):
            raise ValidationError('Phone number is not valid')
        return value
    
    
class UserVeifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    otp = serializers.CharField(max_length=4)

    def validate_phone_number(self, value):
        if not (value.startswith('09') and value.isnumeric() and len(value)==11):
            raise ValidationError('Phone number is not valid')
        return value
        
    def validate_otp(self, value):
        if not (value.isnumeric() and len(value)==4):
            raise ValidationError("otp is not valid")
        return value
    

class PostCrudSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = models.PostCrud
        fields = ["title", "text"]
