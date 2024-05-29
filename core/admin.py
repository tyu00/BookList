from django.contrib import admin
from .models import Book, Author, Genre, User


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(User)
