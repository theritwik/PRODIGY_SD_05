import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP request to the website
url = "http://books.toscrape.com/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product items on the page
product_items = soup.find_all('article', class_='product_pod')

# Create a CSV file to store the data
with open('products.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price", "Rating"])  # header row

    # Extract product information from each item
    for item in product_items:
        title = item.find('h3').text
        price = item.find('p', class_='price_color').text
        rating = item.find('p', class_='star-rating').get('class')[1]

        # Write the data to the CSV file
        writer.writerow([title, price, rating])

print("Data extracted and saved to products.csv")
