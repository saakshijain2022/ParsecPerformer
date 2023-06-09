import requests
from bs4 import BeautifulSoup

# To keep things simple and also reproducible, consider the following HTML code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, "lxml")

# print out nicely formatted HTML
print(soup.prettify())

# Finds the first occurrence of usage for a "b" bold tag.
print(soup.b)

# The "find" function also does the same, where it only finds the first occurrence in the HTML doc
# of a tag with "b".
print(soup.find('b'))

# If we want to find all of the elements on the page
# with the "b" tag, we can use the "find_all" function.
print(soup.find_all('b'))
# it returns a list 

# Name:

# This gives the name of the tag. In this case, the 
# tag name is "b".
print(soup.b.name)

# We can alter the name and have that reflected in the
# source. For instance:
tag = soup.b
print(tag)
tag.name = "blockquote"
print(tag)
print(soup.prettify())

# attributes
# tag= soup.find_all('b')[2]
# getting second
# print(tag)
# print(tag['id'])


# tag = soup.find_all('b')[3]
# print(tag)
# print(tag['another-attribute'])


# We can also use Python's del command for lists to
# remove attributes:
#del tag['id']
#del tag['another-attribute']
#print(tag)

# Multi-valued Attributes
tag = soup.find_all('b')[2]
print(tag)
print(tag.string)
# We can use the "replace_with" function to replace
# the content of the string with something different:
tag.string.replace_with("This is another string")
print(tag)