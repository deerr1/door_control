from django.contrib import admin


from .models import ControlParlors,Parlors,Profile,Types,Requests
# Register your models here.

admin.site.register(ControlParlors)
admin.site.register(Parlors)
admin.site.register(Profile)
admin.site.register(Types)
admin.site.register(Requests)