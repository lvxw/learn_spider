# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

# soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'html5lib')
soup = BeautifulSoup(html, 'lxml')

# print(soup.prettify())
# print(type(soup.title))
# print(soup.title)
# print(soup.title.string)
# print(soup.title.parent)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(type(soup.find_all('a')[0]))
# print(type(soup.a.get('href')))
# print(soup.get_text)
print(type(soup.a.string))