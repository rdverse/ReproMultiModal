from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import requests

import os 
os.chdir("reproducibility/acm_full_pdfs/html1")
import codecs

# div = soup.findAll("script")
# print(div)

# classes = []
# for element in soup.find_all(class_=True):
#     classes.extend(element["class"])

# for link in BeautifulSoup(f, parse_only=SoupStrainer('container'), features= "lxml"):
#     print(link)
#     if link.has_attr('href'):
#         print(link['href'])
hits = list()
acmTags = ["Artifacts Evaluated & Functional", "Results Validated" , "Results Reproduced", "Results Replicated", "Artifacts Evaluated & Reusable"]
allTags = list()
for file in os.listdir("."):
    print(file)
    f=codecs.open(file, 'r')
    # print(f.read())
    soup = BeautifulSoup(f, 'html.parser')
    hits = list()

    with open(file) as fp:
        elements =soup.findAll("a", {"class": "img-badget"})
        for hit in elements:
            hit = hit.text.strip()
            # print(hit)
            hits.append(hit)
        tags = [h for h in hits if h in acmTags]
        print(tags)
        allTags.extend(tags)

from collections import Counter
print(Counter(allTags))

    # print("els {}".format(els.findAll()))


# request = urllib3.Request("testHTML/test.html")
# response = urllib3.urlopen(request)
# soup = BeautifulSoup.BeautifulSoup(response)

# myList = []
# div = soup.findAll('tr', {"class":"formRowLight"})
# for line in div:
#     text= div.findNext('td',{"class":"formRowLight"}).text
#     mylist.append(text)

# print(myList)