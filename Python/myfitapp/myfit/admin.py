from django.contrib import admin

from .models import Device, Device_Owner

admin.site.register(Device)

class Device_OwnerAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'date_of_birth', 'age', 'sex','heart_rate_rest')
    list_display = ('name', 'surname', 'date_of_birth', 'age', 'sex', 'heart_rate_rest')

admin.site.register(Device_Owner, Device_OwnerAdmin)
