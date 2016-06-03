from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import CustomUser

admin.site.site_header = 'DCMS administration'


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email', 'pesel', 'date_of_birth',
        )}),
        (_('Contact details'), {'fields': (
            'city', 'post_code', 'address', 'telephone',
        )}),
        (_('Medical details'), {'fields': ('is_doctor', 'medical_right_number',
        )}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups',
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
