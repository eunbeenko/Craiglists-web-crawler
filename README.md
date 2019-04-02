Scrape:

        At the beginning, I used Anaconda to launch Jupyter Notebook, then used Python3.

        Jupyter Notebook shows the codes for using BeautifulSoup to scrape the data.
        (later I changed the codes in Django to scrape using Regex)

MVC framework:

        Then I set up Django MVC framework.

        After set up Django, I built up the DB, search engine with pagination with django.
        
Display of data to web:

        When displaying the data with html, the first page showing up is the 1000 fetched dataset from the craigslist website         
        http://newyork.craigslist.org/search/bka

        There are 10 pages, so each page contains 100 items of books.

        The first column is just the book id which gave each book an id. (It's not from the website)

        The second column is the book title and the last column is the book's price with US dollar.

        The "Search Title" engine will search the title and show the result with pagination.

        "link to book lists" will go back to the main dataset page.

        "link to drop" will drop all the books, which cleans the database.

        Go back the the book lists will show "link to fetch" and this will refetch the booklists with most updated book lists.

Deploy:

        I have deloyed the search engine on AWS. 
        
        I used cron to update data every 24 hours.
        
        link: http://18.221.103.166:8000/craglists/
