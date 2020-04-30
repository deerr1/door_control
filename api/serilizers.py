# from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ControlParlors,Parlors,Profile,Types,Requests
# UserModel = get_user_model()

# class ModifiedUserDetailsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserModel
#         fields = ('pk', 'username', 'email', 'first_name', 'last_name')
#         read_only_fields = ('email', )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_superuser','username',]

class ControlParlorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlParlors
        fields = '__all__'
        depth = 1

class ProfileSerializers(serializers.ModelSerializer):
    ser = UserSerializer(many=False, read_only=True)
    parlors = ControlParlorsSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'

class RequestsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'

class ParlorsSerializers(serializers.ModelSerializer):     
    class Meta:
        model = Parlors
        fields = '__all__'

class TypesSerializers(serializers.ModelSerializer):  
    class Meta:
        model = Types
        fields = '__all__'


