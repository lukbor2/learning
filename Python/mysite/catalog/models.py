from django.db import models
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        """
        String representing the object
        """
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    #In this implementation a book can have only one Author, not many.
    #When an Author is deleted the field in the book object is set to NULL.
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.CharField(max_length=1000, help_text='Enter a short summary of what the book is about')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Characters <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a Genre for this book')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        For this to work we will have to define a URL mapping that has the name book-detail, and define an associated view and template
        """
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Unique ID for this instance of the book')
    book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True, blank = True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default = 'm', help_text = 'Book Availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.id.book.title)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null = True, blank = True)
    date_of_death = models.DateField('Died', null = True, blank = True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
