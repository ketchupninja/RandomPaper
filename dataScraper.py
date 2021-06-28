import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import random

import requests
import json
import time


class Paper:
    def __init__(self):
        self.title = ""
        self.authors = []
        self.abstract = ""
        self.pdfLink = ""
        self.primarySubject = ""
        
def getRandomPaper():

    types = ['gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th', 'math-ph', 'nlin', 'nucl-ex', 'nucl-th','physics','quant-ph', 'astro-ph', 'math', 'q-bio', 'q-fin', 'stat', 'eess', 'econ']

    x = random.randint(0, (len(types) - 1))

    subj = types[x]
    url = 'https://arxiv.org/list/' + subj + '/new'

    post_data = {}
    
    headers = {
    'Host': 'arxiv.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://arxiv.org/archive/' + subj,
    'Upgrade-Insecure-Requests': '1'
    }
    
    response = requests.post(url, headers=headers, data=post_data)    
    soup = BeautifulSoup(response.content)

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
    #print("Returning paper...")
    
    return p
        