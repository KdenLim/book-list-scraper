Python script using Selenium and BeautifulSoup that scrapes a [book list](https://www.jordanbpeterson.com/books/) and converts it to a markdown table (I use it as a to read list in Obsidian).
The script collects each book's title, author, number of pages, and cover image.


**How it works:**

    1) Loads the book list page and clicks Load More until all books are visible.

    2) Extracts Amazon links for each book.

    3) Scrapes book details from Amazon.

    4) Exports everything into a Markdown-formatted table.

