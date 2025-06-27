from django.contrib import admin
from .models import OtherUsers, PetGender, PetData

# Register your models here.

admin.site.register(OtherUsers)
admin.site.register(PetGender)
admin.site.register(PetData)