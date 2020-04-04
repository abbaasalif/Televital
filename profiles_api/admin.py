from django.contrib import admin
from profiles_api import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileVitals)
admin.site.register(models.ActualVitals)
