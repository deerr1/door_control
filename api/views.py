from django.shortcuts import render
from rest_framework import generics
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import jwt
import json

from .models import Profile, Parlors, Types
from .serilizers import ProfileSerializers, ParlorsSerializers, TypesSerializers

# Create your views here.

method_decorator = method_decorator(csrf_protect)

def cheak_jwt(jw):
    try:
        jw = jwt.decode(jw, settings.SECRET_KEY , algorithms='HS256')
        return jw['user_id']
    except:
        return -1


class ProfileList(generics.ListAPIView):

    filt = -1
    queryset = Profile.objects.all().filter(ser=filt)
    serializer_class = ProfileSerializers
    
    def post(self, request, *args, **kwargs):
        
        data = request.data
        custom_decks = data['jwt']
        filt = cheak_jwt(custom_decks)
        self.queryset = Profile.objects.all().filter(ser=filt)
        return self.list(request, *args, **kwargs)

class CreateReq(generics.ListCreateAPIView):
    
    queryset = Parlors.objects.all()
    
    serializer_class = ParlorsSerializers
   
    def get(self, request, *args, **kwargs):
        # self.queryset = [list(self.queryset), list(Types.objects.all())]


        # return HttpResponse(list(Types.objects.all()))
        return self.list(request, *args, **kwargs) 


    def post(self, request, *args, **kwargs):

        data = request.data
        custom_decks = data['jwt']
        filt = cheak_jwt(custom_decks)

        return self.create(request, *args, **kwargs)