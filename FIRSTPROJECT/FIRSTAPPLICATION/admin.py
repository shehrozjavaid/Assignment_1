from django.contrib import admin
from .models import Name,Address,ID,Contact 
# Register your models here.
admin.site.register(Name)
admin.site.register(Address)
admin.site.register(ID)
admin.site.register(Contact)