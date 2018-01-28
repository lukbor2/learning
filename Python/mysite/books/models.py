from django.db import models
import datetime

# Create your models here.

class Publisher (models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    # headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_NULL,))
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def _get_book_info(self):
        """Example of a model method."""
        return '%s %s %s' % (self.title, self.publisher, self.publication_date.strftime('%m%d%Y'))

    book_info = property(_get_book_info)
