from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import CustomUser

admin.site.site_header = 'DCMS administration'

admin.site.register(CustomUser, UserAdmin)
