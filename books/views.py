from django.shortcuts import render

from .models import Book


def index(request):
    bbs = Book.objects.all()
    len_books = len(bbs)
    return render(request, 'books/index.html', {'bbs': bbs, 'len_books': len_books})
