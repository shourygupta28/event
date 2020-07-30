from django.contrib import admin
from .models import Company, Trading, Share

admin.site.register(Company)
admin.site.register(Trading)
admin.site.register(Share)

# Register your models here.
