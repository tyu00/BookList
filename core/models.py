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
    read_status = models.CharField(max_length=20, choices=[
        ('read', 'Прочитано'),
        ('unread', 'Не прочитано'),
        ('postponed', 'Отложено')
    ], default='unread')
    ratings = models.ManyToManyField('Book', through='Rating', related_name='rated_by_users')
    reviews = models.ManyToManyField('Book', through='Review', related_name='reviewed_by_users')
    bookmarks = models.ManyToManyField('Book', through='Bookmark', related_name='bookmarked_by_users')
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='user',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Rating(models.Model):
    rating = models.IntegerField('Оценка')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_given')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ['rating']
        unique_together = ('user', 'book')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
        unique_together = ('user', 'book')


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks_created')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'
        unique_together = ('user', 'book')
