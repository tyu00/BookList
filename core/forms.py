from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Author, User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'content', 'cover', 'publication_date', 'author', 'genre')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'birth_date')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    pass
