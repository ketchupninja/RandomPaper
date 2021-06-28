from flask import Flask
import dataScraper
import json

app = Flask(__name__)

#Func will run on main page, URL "/"
@app.route('/')
def randpaper():
    paper = dataScraper.getRandomPaper()
    
    paperAsDict = {'title': paper.title, 'authors': paper.authors, 'abstract':paper.abstract, 'primarySubject':paper.primarySubject, 'pdfLink':paper.pdfLink}
    
    paperjson = json.dumps(paperAsDict)
    
    return paperjson


if __name__ == '__main__':
    app.run()