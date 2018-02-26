from django.contrib import admin

from .models import Device, Device_Owner

class Device_OwnerAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'date_of_birth', 'age', 'sex','heart_rate_rest')
    list_display = ('name', 'surname', 'date_of_birth', 'age', 'sex', 'height', 'weight', 'heart_rate_max', 'heart_rate_rest')

admin.site.register(Device_Owner, Device_OwnerAdmin)

class DeviceAdmin(admin.ModelAdmin):
    fields = ('device_serial_no', 'device_name', 'device_model', 'device_owner')
    list_display = ('device_serial_no', 'device_name', 'device_model')

admin.site.register(Device, DeviceAdmin)
