from django.contrib import admin
from .models import Task,Category,Product



# Register models
admin.site.register([Task,Category])
admin.site.register(Product)