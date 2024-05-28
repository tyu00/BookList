from django import forms
from .models import Book, Author, Genre


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'birth_date')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'content', 'cover', 'publication_date', 'author', 'genre')
