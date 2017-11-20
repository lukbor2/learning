import os
import sys
import django

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
	django.setup()
	
	from polls import models	
		
	#Create and save some publications.
	
	p1 = models.Publication(title='The Python Journal')
	p2 = models.Publication(title='Science News')
	p3 = models.Publication(title='Science Weekly')

	p1.save()
	p2.save()
	p3.save()
	
	print(models.Publication.objects.all())
	models.Publication.objects.all().delete()
	print(models.Publication.objects.all())
