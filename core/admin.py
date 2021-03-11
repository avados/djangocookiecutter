from django.contrib import admin

from .models import Ccm


class CcmAdmin(admin.ModelAdmin):
    model = Ccm


admin.site.register(Ccm, CcmAdmin)
