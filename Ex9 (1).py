import urllib2 
from bs4 import BeautifulSoup

brewery = "http://www.brewerydb.com/styles"
page = urllib2.urlopen(brewery).read()
soup = BeautifulSoup(page, "lxml")

links = []

for i in range(1, 170):
    links.append("http://www.brewerydb.com/style/" + str(i))

for l in links:
    print l
    p = urllib2.urlopen(l).read()
    s = BeautifulSoup(p, "lxml")
    s.find_all('div class="description')
    

users_keywords = raw_input('Insert comma seperated beer keywords: ').split(',')


print users_keywords
