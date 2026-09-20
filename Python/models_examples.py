from django.db import models

#Examples of how to use the Many-To-Many API.

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering('headline',)

#Create a couple of publications.

p1 = Publication(title='The Python Journal')
p2 = Publication(title='Science News')
p3 = Publication(title='Science Weekly')

p1.save()
p2.save()
p3.save()