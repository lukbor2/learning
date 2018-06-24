from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class AuthorAdmin (admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
	# This is used to show instances of BookInstance when I access a book.
	model = BookInstance

@admin.register(Book)
class BookAdmin (admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline] # This is used to show instances of BookInstance when I access a book.

@admin.register(BookInstance)
class BookInstanceAdmin (admin.ModelAdmin):
	list_display = ('book', 'status','borrower', 'due_back', 'id')
	list_filter = ('status', 'due_back')
	fieldsets = (
		('About the Book', {
			'fields': ('book', 'imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back', 'borrower')
		}),
	)
