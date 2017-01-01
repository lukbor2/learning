from django.db import models
from datetime import date
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Patient(models.Model):
    """ 
    Each patient will be linked to one or more measures.
    Each measure is linked to one and only one patient.
    I use the package django-etc to use the verbose name in situations like table headers. So I control from the model the label used for the field.
    """
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(max_length=255, verbose_name='Last Name')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    age = models.IntegerField(blank=True, null=True, verbose_name='Age')
    email = models.EmailField(blank=True, verbose_name='e-mail')

    # Decorating this method as a property allows me to call it from a template.
    # So I can calculate the age when it is displayed.
    # There is no need to save the age in the db, because it can always be calculated based on the date of birth.
    # Just for the sake of learning, I did use the signals to calculate the age and save it. Look at the method further down.
    @property
    def calculate_age(self):
        return (date.today().year - self.date_of_birth.year)

    def __str__(self):
        return '%s %s %s'  % (self.first_name, self.last_name, self.date_of_birth.strftime('%m-%d-%Y'))
    
    def get_absolute_url(self):
        # I need this method because it is used in the PatientCreate view to return the url to go when the form used to create a patient is successfully processed.
        # Note that I have to specify the app name, otherwise it does not work. I did not understand why.
        return reverse('bptrack:patient-detail', kwargs={'pk': self.pk})

    # remember that Model metadata is “anything that’s not a field”, such as ordering options
    class Meta:
        ordering = ['last_name', 'first_name']

class BP_Measure(models.Model):
    """ 
    Each patient will be linked to one or more measures.
    Each measure is linked to one and only one patient.
    BP measures (min and max) are expected in mmHg.
    Date, min, max and pulse are all mandatory fields.
    """
    TIME_OF_DAY = (
        ('MO', 'Morning'),
        ('AF', 'Afternoon'),
        ('EV', 'Evening'),
        )
    
    patient = models.ForeignKey(Patient)
    bp_measure_date = models.DateField(blank=False, default=date.today, help_text='Day when the measure was taken')
    bp_measure_min = models.IntegerField(blank=False, help_text='Min pressure in mmHG')
    bp_measure_max = models.IntegerField(blank=False, help_text='Max pressure in mmHG')
    bp_measure_pulse = models.IntegerField(blank=False, help_text='Pulse when the measure was taken')
    bp_measure_time_of_day = models.CharField(blank=False, max_length=30, choices=TIME_OF_DAY, help_text='Pick one of the categories depending on the time when the measure was taken')
    bp_measure_note = models.CharField(blank=True, null=True, max_length=255, help_text= 'Free text')

    def __str__(self):
        return '%s %s %d %d %d %s' % (self.patient, self.bp_measure_date.strftime('%m-%d-%Y'), self.bp_measure_min, self.bp_measure_max, self.bp_measure_pulse, self.bp_measure_note)
    
"""
Even if it does not make sense to save the age in the db, I wanted to learn how to do something before an instance is
saved and also how to save the result of this "something" in the db.
It turns out the best way to do it are the signals.
Basically, pre_save is a signal and with the method below I intercept the signal and do something before the instance is saved.
"""
@receiver(pre_save, sender=Patient)
def set_age(sender, instance, **kwargs):
    instance.age = (date.today().year - instance.date_of_birth.year)
