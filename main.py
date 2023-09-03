import requests
import time
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import numpy as np
import re

# print("Preparing for scraping...")
url = 'https://www.daraz.com.np/products/apple-macbook-air-13-in-with-m1-chip256gb-with-1-year-breakage-insurance-evostore-i105118187-s1026752551.html'
# print('Requesting page content...')
# print('URl: ', url)
page = requests.get(url, timeout=1000, headers={'User-Agent': 'Mozilla/5.0'})
# print("Request Status Code: ", page.status_code)
if page.status_code == 200:
    # print("Page content received successfully.")
    ...
else:
    ...
    # print("Error: ", page.status_code)
    exit(0)
# print('Processing page content...')
soup = bs(page.content, 'html.parser')

product_name = soup.find('span', class_='pdp-mod-product-badge-title')
price_section_content = soup.find('div', class_='pdp-product-price')

print(soup.prettify())
# Product details
# print('Product details')
# print('Product Name: ', product_name)
# print(price_section_content)

