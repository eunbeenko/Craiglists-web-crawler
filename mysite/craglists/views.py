from django.shortcuts import render
from .models import Book
from bs4 import BeautifulSoup
from requests import get


def index(request):
    latest_book_list = Book.objects.order_by('id')[0:1000]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'craglists/index.html', context)


def search(request):
    latest_book_list = Book.objects.order_by('id')[0:1000]
    context = {
        'latest_book_list': latest_book_list,
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