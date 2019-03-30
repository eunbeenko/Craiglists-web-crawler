from django.shortcuts import render
from .models import Book
from bs4 import BeautifulSoup
from requests import get
import math


def index(request):
    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET['page'])
        start = (page-1)*100
        end = page*100
    else:
        start = 0
        end = 100
    latest_book_list = Book.objects.order_by('id')[start:end]
    context = {
        'latest_book_list': latest_book_list,
        'pages': range(1, 11)
    }
    return render(request, 'craglists/index.html', context)


def search(request):
    search_text = request.GET['title']
    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET['page'])
        start = (page-1)*100
        end = page*100
    else:
        start = 0
        end = 100
    list = Book.objects.filter(title__icontains=search_text)
    count = list.count()
    result = list[start:end]

    context = {
        'latest_book_list': result,
        'pages': range(1, math.ceil(count/100)),
        'search_text': search_text,
    }
    return render(request, 'craglists/search.html', context)


def fetch(request):
    pages = ["", "?s=120", "?s=240", "?s=360", "?s=480", "?s=600", "?s=720", "?s=840", "?s=960", "?s=1080"]

    for x in pages:
        url = 'https://newyork.craigslist.org/search/bka' + x
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)
        books = html_soup.find_all('li', class_='result-row')

        for every_book in books:
            name = every_book.p.a.text
            price = every_book.p.find('span', class_='result-price').text
            b = Book(title=name, price=price)
            b.save()

    return render(request, 'craglists/fetch.html')


def drop(request):
    Book.objects.all().delete()
    return render(request, 'craglists/drop.html')