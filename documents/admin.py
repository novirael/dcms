from django.contrib import admin

from documents.models import Referral, Prescription, Receipt


admin.site.register(Referral)
admin.site.register(Prescription)
admin.site.register(Receipt)
