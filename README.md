# Book Scraper - Web Scraping Project

This Python script scrapes book data (title, price, and rating) from the website [Books to Scrape](http://books.toscrape.com/). The scraped data is then saved into a CSV file for easy access and further analysis.

## Features

- **Web Scraping**: The script sends an HTTP request to the website and parses the HTML content using BeautifulSoup.
- **Data Extraction**: Extracts book title, price, and rating from the webpage.
- **CSV Output**: Stores the extracted data in a CSV file (`products.csv`), including the book's title, price, and rating.

## Libraries Used

- `requests`: For sending HTTP requests to the website and fetching the HTML content.
- `BeautifulSoup` (`bs4`): For parsing the HTML content and extracting information.
- `csv`: For writing the scraped data into a CSV file.

## How It Works

1. **Send HTTP Request**: The script sends a request to the website URL using the `requests` library.
2. **Parse HTML**: The response is parsed using BeautifulSoup to extract relevant book data (title, price, and rating).
3. **Extract Data**: For each book on the page, the script extracts:
   - Title of the book.
   - Price of the book.
   - Rating of the book (represented by star ratings).
4. **Save to CSV**: The extracted data is written to a CSV file called `products.csv`.

## Example

Sample output stored in `products.csv`:

```csv
Title,Price,Rating
"A Light in the Attic","£51.77","Three"
"Tipping the Velvet","£53.74","One"
"Soumission","£50.10","One"
"Sharp Objects","£47.82","Four"
...
