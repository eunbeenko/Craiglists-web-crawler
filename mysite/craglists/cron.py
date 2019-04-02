from .models import Book
from requests import get
import re

def fetch():
    pages = ["", "?s=120", "?s=240", "?s=360", "?s=480", "?s=600", "?s=720", "?s=840", "?s=960", "?s=1080"]

    for x in pages:
        url = 'https://newyork.craigslist.org/search/bka' + x
        response = get(url)
        response_line = re.split('\n', response.text)
        stripped_line = ''

        for line in response_line:
            stripped_line += line.lstrip()

        relevant = re.findall('<ul class="rows">(.*?)</ul>', stripped_line)
        books = str(relevant).split('</p></li>') # All books end with this tag

        for line in books:
            title = re.findall('class="result-title hdrlnk">(.*?)</a>', line)
            price = re.findall('class="result-price">\$(.*?)</span>', line)
            try:
                instance, created = Book.objects.update_or_create(title=title[0], price=price[0])
                if created: # Checks for duplicates
                    instance.save()
                else:
                    pass
            except:
                pass



if __name__ == "__main__":
    fetch()
