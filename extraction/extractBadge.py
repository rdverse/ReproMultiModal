from re import A
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import requests
import pprint
import os 
import numpy as np
import pandas as pd
import codecs
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.preprocessing import MultiLabelBinarizer

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
acmTags = ["Artifacts Evaluated & Functional", "Artifacts Evaluated & Reusable", "Results Reproduced",
             "Artifacts Evaluated", "Artifacts Available",
             "Results Validated" , "Results Replicated", "Results Reproduced"]

UacmTags = ["Artifacts Available",
"Artifacts Evaluated & Reusable",
"Artifacts Evaluated & Reusable / v1.1",
"Artifacts Available / v1.1",
"Artifacts Evaluated & Functional / v1.1",
"Results Reproduced / v1.1",
"Artifacts Evaluated & Functional",
"Best Paper",
"Results Reproduced",
"Distinguished Paper",
"Best Student Paper",
"Best Artifact",
"Best Industry Paper"]

allTags = list()
allHits = list()
allFiles = list()
allTagLabels = list()

os.chdir("reproducibility/acm_full_pdfs/html1")
def get_rcParams(plt):
    plt.rcParams['font.size'] = 12
    plt.rcParams['hatch.linewidth'] = 0.25
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Times New Roman'
    plt.rcParams['figure.dpi'] = 600
    plt.rcParams["lines.linewidth"] = 1
    plt.rcParams['hatch.linewidth'] = 0.15
    return plt

def plot_frequency(allTagLabels,plt):
    #prepare data
    counts = [len(lab) for lab in allTagLabels]
    ccounts = Counter(counts)
    
    # rcparams
    plt = get_rcParams(plt)
    #plot
    plt.bar(list(ccounts.keys()), list(ccounts.values()))
    plt.xticks([0,1,2,3,4])
    plt.xlabel("Number of tags per scholarly article")
    plt.ylabel("Frequency")
    fig = plt.gcf()
    fig.set_size_inches(3,3)
    plt.tight_layout()

    plt.savefig("/home/devesh/Code/ReproMultiModal/figures/data/labelcounts.png")

def get_tag_hits():
    for file in os.listdir("."):
        print(file)
        f=codecs.open(file, 'r')
        # print(f.read())
        soup = BeautifulSoup(f, 'html.parser')
        hits = list()
        allFiles.append(file)
        with open(file) as fp:
            elements =soup.findAll("a", {"class": "img-badget"})
            for hit in elements:
                hit = hit.text.strip()
                # print(hit)
                hits.append(hit)

            hits = [hit.strip(" / v1.1") for hit in hits]
            hits = list(set(hits))
            tags = [hit for hit in hits if hit in UacmTags]
            tags = list(set(tags))
            # print(tags)
            allTags.extend(tags)
            allTagLabels.append(tags)    
            allHits.extend(hits)
    
    return allTags, allTagLabels, allHits, allFiles

allTags, allTagLabels, allHits, allFiles = get_tag_hits()

print(pprint.pprint(Counter(allTags)))
print(Counter(allHits))

mlb = MultiLabelBinarizer()
labels = mlb.fit_transform(allTagLabels)

plot_frequency(allTagLabels,plt)

# sns.

# create dataset
classLabels = list(mlb.classes_)
classLabels.insert(0,"fileName")
data = np.hstack((np.array(allFiles).reshape(-1,1), labels))
df = pd.DataFrame(data, classLabels)

df.to_csv("labelData.csv")

    # print("els {}".format(els.findAll()))


# request = urllib3.Request("testHTML/test.html")
# response = urllib3.urlopen(request)
# soup = BeautifulSoup.BeautifulSoup(response)

# myList = []
# div = soup.findAll('tr', {"class":"formRowLight"})
# for line in div:
#     text= div.findNext('td',{"class":"formRowLight"}).textdistBetweendistBetween