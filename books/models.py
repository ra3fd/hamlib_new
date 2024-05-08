
from django.db import models


class Book(models.Model):
    bookname = models.CharField(max_length=60, verbose_name='Название книги')
    author = models.CharField(max_length=50, blank=True, verbose_name='Автор')
    year = models.CharField(max_length=4, blank=True, verbose_name='Год изд.')
    pages = models.CharField(max_length=4, blank=True, verbose_name='Страниц')
    registered = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Зарегистрировано')
    comment = models.TextField(blank=True, verbose_name='Комментарии')

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'книгу'
        ordering = ['year']
