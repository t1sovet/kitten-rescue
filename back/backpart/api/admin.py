from django.contrib import admin

from api.models import Address, Kitten, Message

# Register your models here.
admin.site.register(Kitten)
admin.site.register(Address)    
admin.site.register(Message)