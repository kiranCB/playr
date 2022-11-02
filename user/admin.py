from django.contrib import admin
from user import models
# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.AddressModel)
admin.site.register(models.LocationModel)
admin.site.register(models.ProfileModel)