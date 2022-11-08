#Installing the lxml module, which is necessary for reading HTML content with Pandas; otherwise, Python throws an ImportError exception

# pip install lxml
import pandas


#Reading HTML content from an URL

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
d = pandas.read_html(url)


#If there are multiple tables on the page, you can select which one to load/read by using indexes

d = pandas.read_html(url)[0]
d = pandas.read_html(url)[1]
