import requests
from bs4 import BeautifulSoup

# URL of the product page
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

def scrape_book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_page_url = url
    upc = soup.find('th', text='UPC').find_next_sibling('td').text
    book_title = soup.find('h1').text
    price_including_tax = soup.find('th', text='Price (incl. tax)').find_next_sibling('td').text

    price_excluding_tax = soup.find('th', text='Price (excl. tax)').find_next_sibling('td').text
    quantity_available = soup.find('th', text='Availability').find_next_sibling('td').text.strip()
    product_description = soup.find('div', id='product_description').find_next_sibling('p').text


    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].find('a').text
    review_rating = soup.find('p', class_='star-rating')['class'][1]

    image_url = soup.find('img')['src']
    image_url = 'http://books.toscrape.com/' + image_url.replace('../', '')

    print(f"Product Page URL: {product_page_url}")
    print(f"UPC: {upc}")
    print(f"Book Title: {book_title}")
    print(f"Price (including tax): {price_including_tax}")
    print(f"Price (excluding tax): {price_excluding_tax}")
    print(f"Quantity Available: {quantity_available}")
    print(f"Product Description: {product_description}")
    print(f"Category: {category}")
    print(f"Review Rating: {review_rating}")
    print(f"Image URL: {image_url}")

scrape_book_info(url)
