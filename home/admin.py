from django.contrib import admin
from .models import Company, Trading, Share, Bidding

admin.site.register(Company)
admin.site.register(Trading)
admin.site.register(Share)
admin.site.register(Bidding)

# Register your models here.
