from django.db import models
from .book import Book
from .category import Category


class BookCategory(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
