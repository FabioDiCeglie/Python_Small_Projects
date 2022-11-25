import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")


text = webpage.text

content = webpage.content
# print(content)

result = BeautifulSoup(content, "html.parser")
# print(result)

# h = result.head


# h2 = result.h2
# # print(h2)

# title = result.title

# header = result.header
# title.name = "mytitle"
# print(title)

# print(h.prettify())
# print(result.header['role'])

# result.header['role'] = "something"
# print(result.header['role'])

#or, using the get() method:
# >>> header.get('role')
# 'banner'
# # >>> header.get('class')
# ['navbar', 'navbar-fixed-top', 'navbar-static']


#Adding a new tag attribute
# >>> header['new'] = "python"
# >>> header.attrs
# {'role': 'something', 'class': ['navbar', 'navbar-fixed-top', 'navbar-static'], 'new': 'python'}

#Removing a tag attribute
# >>> del header['new']
# >>> header.attrs
# {'role': 'something', 'class': ['navbar', 'navbar-fixed-top', 'navbar-static']}

#Extracting the string from a tag
# >>> h2 = result.h2
# >>> h2
# <h2>Top items being scraped right now</h2>
# >>> h2.string
# 'Top items being scraped right now'
# >>> type(h2.string)
# <class 'bs4.element.NavigableString'>
#this is called a NavigableString
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigablestring

#Zooming in to a certain area of the HTML tree
#Using a tag name as an attribute will give you only the first tag by that name
#More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
# result.header.div
# result.header.div.div.a
# result.header.div.div.a.button


# find and find_all()

#The find_all() method - finds the all occurrences of a certain tag (and other features, e.g. class name)

# result.find("div").prettify()

# print(len(result.find_all("h1")))

products = result.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"})

# print(type(products))
print(len(products))
