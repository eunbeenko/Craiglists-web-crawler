from django.shortcuts import render

from .models import Book


def index(request):
    latest_book_list = Book.objects.order_by('title')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'craglists/index.html', context)


def fetch(request):
    return render(request, 'craglists/fetch.html')


def drop(request):
    return render(request, 'craglists/drop.html')
