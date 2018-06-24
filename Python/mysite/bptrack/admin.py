from django.contrib import admin
from .models import Patient, BP_Measure
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    search_fields = ('first_name', 'last_name')

class BP_MeasureAdmin(admin.ModelAdmin):
    list_display = ('patient', 'bp_measure_date', 'bp_measure_time_of_day', 'bp_measure_min', 'bp_measure_max', 'bp_measure_pulse', 'bp_measure_note')
    #TODO: find out how to filter the measures by patient in the Admin portal. There are filtering features available.

admin.site.register(Patient, PatientAdmin)
admin.site.register(BP_Measure, BP_MeasureAdmin)
