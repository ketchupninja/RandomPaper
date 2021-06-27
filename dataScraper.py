import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import random

class Paper:
    def __init__(self):
        self.title = ""
        self.authors = []
        self.abstract = ""
        self.pdfLink = ""
        self.primarySubject = ""
        

myPath = os.getcwd() + "\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=myPath)




types = ['gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th', 'math-ph', 'nlin', 'nucl-ex', 'nucl-th','physics','quant-ph', 'astro-ph', 'math', 'q-bio', 'q-fin', 'stat', 'eess', 'econ']

x = random.randint(0, (len(types) - 1))

subj = types[x]
url = 'https://arxiv.org/list/' + subj + '/new'
driver.get(url)


content = driver.page_source
soup = BeautifulSoup(content)

#Use synced indices to build objects in sequence later
titles = []
authors = []
abstracts = []
pdfLinks = []
primarySubjects = []


for element in soup.findAll():
    prop = element.attrs #{category : value of category}

    if 'Download PDF' in list(prop.values()):
        #print(list(prop.values()))
        link = 'https://arxiv.org/' + list(prop.values())[0]
        pdfLinks.append(link)
    
    if ['mathjax'] in list(prop.values()):
        #print(element.text)
        abstracts.append(element.text)
    
    if ['list-title', 'mathjax'] in list(prop.values()):
        #print(element.text[7:])
        titles.append(element.text[7:])
    
    if ['list-authors'] in list(prop.values()):
        #print(element.text[10:(len(element.text)-1)])
        authors.append(element.text[10:(len(element.text)-1)])      
        
    if ['primary-subject'] in list(prop.values()):
        #print(element.text) #Contains a parenthetical at the end on subject, but not important to remove that now
        primarySubjects.append(element.text)
        
papers = []

for i in range(0, len(abstracts)):
    p = Paper()
    
    p.title = titles[i]
    p.authors = authors[i]
    p.abstract = abstracts[i]
    p.primarySubject = primarySubjects[i]
    p.pdfLink = pdfLinks[i]
    
    papers.append(p)
    
    
x = random.randint(0, (len(papers) - 1))

#p is the randomly selected paper
p = papers[x]

print(p.title)
print(p.authors)
print(p.primarySubject)
print(p.abstract)
print(p.pdfLink)
    

        
