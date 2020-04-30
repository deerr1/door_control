
from django.contrib import admin
from django.urls import path, include

from .views import ProfileList,CreateReq

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('listparlors',ProfileList.as_view()),#Запрос на твой список кабинетов
    #Запрос на открытие кабинета
    #Запрос на закрытие кабинета 
    path('createreq', CreateReq.as_view()), #Запрос на создание запроса 
    #Запрос на список запросов от пользователей
    #Разрешение/отклонение запроса, и создание ссылки доступа если это для пользователя
    #Запрос от гостя на открытие кабинета 
    #Запрос от гостя на закрытие кабинета

    
]
