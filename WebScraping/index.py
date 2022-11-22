import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")


text = webpage.text

content = webpage.content
# print(content)

result = BeautifulSoup(content, "html.parser")
# print(result)
