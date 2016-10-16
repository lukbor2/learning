from django.db import models

class Patient(models.Model):
    """ 
    Each patient will be linked to one or more measures.
    Each measure is linked to one and only one patient.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def calculate_age(self):
        #TODO implement a function which calculates the age of the patient based on the date of birth, then set the age attribute based on the calculation.
        pass

    def __str__(self):
        return '%s %s %s'  % (self.first_name, self.last_name, self.date_of_birth.strftime('%m-%d-%Y'))

class BP_Measure(models.Model):
    """ 
    Each patient will be linked to one or more measures.
    Each measure is linked to one and only one patient.
    BP measures (min and max) are expected in mmHg.
    Date, min, max and pulse are all mandatory fields.
    """
    bp_measure_date = models.DateField(blank=False)
    #TODO make the field bp_measure_date mandatory and not null. Default should be today.
    bp_measure_min = models.IntegerField(blank=False)
    bp_measure_max = models.IntegerField(blank=False)
    bp_measure_pulse = models.IntegerField(blank=False)
    bp_measure_note = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return '%s %s %d %d %d %s' % (self.patient, self.bp_measure_date.strftime('%m-%d-%Y'), self.bp_measure_min, self.bp_measure_max, self.bp_measure_pulse, self.bp_measure_note)


