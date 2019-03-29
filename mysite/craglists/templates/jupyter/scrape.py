from bs4 import BeautifulSoup
from requests import get


def get_data():
    title = []
    price = []
    pages = ["", "?s=120", "?s=240", "?s=360", "?s=480", "?s=600", "?s=720", "?s=840", "?s=960", "?s=1080"]

    ## iterate through the pages to collect desired dataset
    for x in pages:
        url = 'https://newyork.craigslist.org/search/bka' + x
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)
        books = html_soup.find_all('li', class_='result-row')

        ## extract all the data from books
        for every_book in books:
            ## collect title of the book:
            name = every_book.p.a.text
            title.append(name)
            title=title[0:1000]
            ## collect price of the book:
            prices = every_book.p.find('span', class_='result-price').text
            price.append(prices)

    return len(title)


print(get_data())
