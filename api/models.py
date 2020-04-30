from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



# кабинет
class Parlors(models.Model):
    number = models.IntegerField()
    section = models.IntegerField()
       
    def __str__(self):
        return '%s/%s' % (self.number, self.section)
#Информация об управляемом объекте
class ControlParlors(models.Model):
    Control_id = models.ForeignKey(Parlors, on_delete=models.CASCADE)
    time_from = models.TimeField(blank=True,null=True)
    time_to = models.TimeField(blank=True,null=True)
    quantity = models.IntegerField(blank=True)

    def __str__(self):
        return '%s %s %s %s' % (self.Control_id, self.time_from, self.time_to, self.quantity)
#Управление кабинетом
class Profile(models.Model):
    ser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parlors = models.ForeignKey(ControlParlors, on_delete=models.CASCADE) # Вопрос, создавать по запросу новую записть в таблице ControlParlors и к ней обращаться, или же искать похожую запись и только потом

#Тип запроса
class Types(models.Model):
    typ = models.CharField(max_length=20)  

    def __str__(self):
        return  '%s' % (self.typ)
#Запросы на доступ к кабинету
class Requests(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parlors = models.ForeignKey(ControlParlors, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    types = models.ForeignKey(Types, on_delete=models.CASCADE)