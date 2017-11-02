# To scrape Project Euler website for problem links in its archive page

from urllib import request

# to handle HTTP requests

from bs4 import BeautifulSoup

# to parse the html data

link = "https://projecteuler.net/archives"

# link we need to visit

site = request.urlopen(link)

# site contains HTTP data received from the link

content = site.read()

# content contains the html code

soup = BeautifulSoup(content,"html.parser")

# soup contains html code in a parsed object; also see: print(soup.prettify()) to print indentated html code

table = soup.find("table",{"id":"problems_table"}) 

# we dont need to use find_all() because after examining the html code, there is only one table with this id

listLinks = table.find_all("a")

# "bs4.element.ResultSet" -> list of all <a></a> tags found under table

problemLinks = [] # to store links to problems

for links in listLinks:
	p = "https://projecteuler.net/"+links.get("href")
	problemLinks.append(p)
	print(p)
