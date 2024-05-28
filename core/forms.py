from django import forms
from .models import Book, Rating, Bookmark, Review


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'content', 'cover', 'publication_date', 'author', 'genre')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('book',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
