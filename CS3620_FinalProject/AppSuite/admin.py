from django.contrib import admin
from .models import Profile, Journal, Hiking

# Register your models here.

admin.site.register(Hiking)
admin.site.register(Journal)
admin.site.register(Profile)
