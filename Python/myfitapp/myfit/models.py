from django.db import models
from datetime import date

class Device_Owner(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F','Female'),
    )
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=False, null=True)
    age = models.IntegerField(blank=True, null=False, default=0)
    sex = models.CharField(max_length=1, choices=SEX)
    height = models.IntegerField(blank=True, null=True) #Assumption: height in cm.
    weight = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=4) #Assumption: weight in KG.
    heart_rate_max = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the max heart rate.
    heart_rate_rest = models.IntegerField(blank=False, null=False, default=0) #This field is needed to do other calculations.
    heart_rate_zone1_low = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone1_high= models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone2_low = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone2_high = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone3_low = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone3_high = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone4_low = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone4_high = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone5_low = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.
    heart_rate_zone5_high = models.IntegerField(blank=True, null=False, default=0) #I will have a method calculating the heart rate zones.

    def __str__(self):
        return '{0} {1} {2}'.format(self.id, self.name,self.surname)

    def get_absolute_url(self):
        """
        Returns the url to access a particular Device_Owner instance.
        For this to work we will have to define a URL mapping that has the name owner-detail, and define an associated view and template
        """
        return reverse('owner-detail', args=[str(self.id)])

class Device(models.Model):
    device_serial_no = models.CharField(primary_key=True, max_length=20)
    device_model = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    device_owner = models.ForeignKey(Device_Owner, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} {2}'.format(self.device_serial_no, self.device_name,self.device_model)

    def get_absolute_url(self):
        """
        Returns the url to access a particular Device instance.
        For this to work we will have to define a URL mapping that has the name device-detail, and define an associated view and template
        """
        return reverse('device-detail', args=[str(self.device_serial_no)])

class Activity(models.Model):
    activity_id = models.CharField(primary_key=True, max_length=20)
    activity_time_original = models.CharField(blank=False, max_length=20)
    activity_date = models.DateField(blank=False, null=False)
    activity_time = models.TimeField(blank=False, null=False)
    activity_duration = models.IntegerField(blank=False, null=False, default=0)
    activity_duration_hh = models.IntegerField(blank=False, null=False, default=0)
    activity_duration_mm = models.IntegerField(blank=False, null=False, default=0)
    activity_duration_ss = models.IntegerField(blank=False, null=False, default=0)
    activity_speed_max = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=3)
    activity_speed_avg = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=3)
    activity_hr_max = models.IntegerField(blank=False, null=False, default=0)
    activity_hr_min = models.IntegerField(blank=False, null=False, default=0)
    activity_hr_avg = models.IntegerField(blank=False, null=False, default=0)
    activity_type = models.IntegerField(blank=False, null=False, default=0)
    activity_type_name = models.CharField(max_length=200, blank=False, null=False)
    activity_device_used = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.activity_id, self.activity_type, self.activity_type_name, self.activity_date, self.activity_duration)

    def get_absolute_url(self):
        """
        Returns the url to access a particular Activity instance.
        For this to work we will have to define a URL mapping that has the name activity-detail, and define an associated view and template
        """
        return reverse('activity-detail', args=[str(self.activity_id)])
