from django.contrib import admin
from .models import Property, Property_lease

# Register your models here.
admin.site.register(Property)
admin.site.register(Property_lease)