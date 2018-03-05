from django.contrib import admin

from .models import Device, Device_Owner, Activity

class Device_OwnerAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'date_of_birth', 'age', 'sex','heart_rate_rest')
    list_display = ('name', 'surname', 'date_of_birth', 'age', 'sex', 'height', 'weight', 'heart_rate_max', 'heart_rate_rest')

admin.site.register(Device_Owner, Device_OwnerAdmin)

class DeviceAdmin(admin.ModelAdmin):
    fields = ('device_serial_no', 'device_name', 'device_model', 'device_owner')
    list_display = ('device_serial_no', 'device_name', 'device_model')

admin.site.register(Device, DeviceAdmin)

class ActivityAdmin(admin.ModelAdmin):
    fields = ('activity_id', 'activity_time_original', 'activity_date', 'activity_time', 'activity_duration', 'activity_duration_hh', 'activity_duration_mm', 'activity_duration_ss', 'activity_speed_max', 'activity_speed_avg','activity_hr_max', 'activity_hr_min', 'activity_hr_avg', 'activity_type', 'activity_type_name', 'activity_device_used')
    list_display = ('activity_id', 'activity_time_original', 'activity_date', 'activity_time', 'activity_duration', 'activity_duration_hh', 'activity_duration_mm', 'activity_duration_ss', 'activity_speed_max', 'activity_speed_avg','activity_hr_max', 'activity_hr_min', 'activity_hr_avg', 'activity_type', 'activity_type_name', 'activity_device_used')

admin.site.register(Activity, ActivityAdmin)
