from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField('Название', max_length=150)
    content = models.TextField('Содержание', blank=True)
    cover = models.ImageField('Обложка', upload_to='photos/%Y/%m/', blank=True, null=True)
    publication_date = models.DateField('Дата публикации')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор', related_name='books')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр', null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['publication_date']

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField('Имя', max_length=150)
    birth_date = models.DateField('Дата рождения', null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField('Жанр', max_length=50, db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['title']

    def __str__(self):
        return self.title


class User(AbstractUser):
    read_status = models.BooleanField(default=False)
