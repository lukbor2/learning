#I am using this script to do some exercises on the Django API to query the records created with Modules.
#I have to add my models to those of an existing APP in order for them to work (I did not understand why).
#I added my models to those belonging to the polls app.

import os
import sys
import django

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
	django.setup()
	
	from polls import models	
	example = 0	
	#Create and save some publications.
	
	p1 = models.Publication(title='The Python Journal')
	p2 = models.Publication(title='Science News')
	p3 = models.Publication(title='Science Weekly')

	p1.save()
	p2.save()
	p3.save()
	print(example, ' Some Publications have been created ...')
	print(models.Publication.objects.all())
	
	#Create an Article
	a1 = models.Article(headline='Django lets you build Web apps easily')
	#Can not add a Publication before it is saved!
	a1.save()
	a1.publications.add(p1)

	#Create another Article and set it appearing in both publications
	example+=1
	
	a2 = models.Article(headline='NASA uses python')
	a2.save()
	a2.publications.add(p1, p2, p3)
		
	print(example, ' Articles being created...')
	print(models.Article.objects.all())

	#All in one step using create.
	new_publication = a2.publications.create(title='Highlights for the children')

	#Accessing the publications from the articles.
	example +=1
	print(example, ' Accessing the publications from the articles')
	print(a1.publications.all())
	print(a2.publications.all())

	#Accessing the articles from the publications.
	example +=1
	print(example, ' Accessing the articles from the publications')
	print(p2.article_set.all())
	print(p1.article_set.all())
	
	#Many-to-many relationships can be queried using lookups across relationships.
	#The following 4 return the same result.
	example +=1
	print(example, ' Querying relatioship using lookups')
	print(models.Article.objects.filter(publications__id=1)) #This does not work because the publication with id=1 is created and then deleted by my cleanup.
	print(models.Article.objects.filter(publications__pk=1)) #This does not work because the publication with id=1 is created and then deleted by my cleanup.
	print(models.Article.objects.filter(publications=1)) #This does not work because the publication with id=1 is created and then deleted by my cleanup.
	print(models.Article.objects.filter(publications=p1))
	
	print(models.Article.objects.filter(publications__title__startswith='Science'))
	print(models.Article.objects.filter(publications__title__startswith='Science').count())
	
	#Reverse m2m queries are supported
	example +=1
	print(example, ' Reverse m2m queries are supported')
	print(models.Publication.objects.filter(article__headline__startswith='NASA'))
	print(models.Publication.objects.filter(article=a1))
	print(models.Publication.objects.filter(article__in=[a1,a2]).distinct())	

	#Adding via the ‘other’ end of an m2m
	example +=1
	print(example, ' Adding via the other end of an m2m')
	a4 = models.Article(headline = 'NASA finds intelligent life on Earth')
	a4.save()

	p2.article_set.add(a4)
	print(p2.article_set.all())
	print(a4.publications.all())

	#Adding via the other end using keywords
	example +=1
	print(example, ' Adding via the other end using keywords')

	new_article = p2.article_set.create(headline='Oxygen-free diet works wonders')
	print(p2.article_set.all())

	#Removing publication from an article
	example +=1
	print(example, ' Removing publication from an article')
	a4.publications.remove(p2)
	print(p2.article_set.all())
	
	#Relation sets can be cleared
	example +=1
	print(example, ' Relation sets can be cleared')
	p2.article_set.clear()
	print(p2.article_set.all())

	#And you can clear from the other end
	example +=1
	print(example, ' And you can clear from the other end')
	p2.article_set.add(a1, a4)
	print(p2.article_set.all())
	print(a4.publications.all())
	a4.publications.clear()
	print(a4.publications.all())
	print(p2.article_set.all())
	


	# Cleaning up....
	print('Cleaning up...')
	models.Publication.objects.all().delete()
	print(models.Publication.objects.all())
	models.Article.objects.all().delete()
	print(models.Article.objects.all())


