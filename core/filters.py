from django_filters import FilterSet, filters
from .models import Book


class BookFilter(FilterSet):
    title = filters.CharFilter(label='название', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title']
