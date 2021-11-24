#coding:utf-8
import os
from bs4 import BeautifulSoup
from folderReader import traverseDIR

def getRootPageURL():
    src = traverseDIR()
    rootPageList = src[0]
    rootPageURL = []
    for item in rootPageList:
        pageName = item.split("/")[-1]
        pageNameURL = ''.join(char for char in pageName if char.isalnum())
        pageNameHTML = "./" + pageNameURL + ".html"
        rootPageURL.append(pageNameHTML)
    return rootPageURL


def postPageBuilder():
    # rootPageURL = getRootPageURL()

    src = traverseDIR()
    rootPageList = src[0]

    htmlSample = ''''''
    soup = BeautifulSoup(htmlSample, 'html.parser')

    posts_start = '''
    {% extends "template.html" %}
    {% block title %}Posts{% endblock %}
    {% block content %}
        <div class="jumbo">
            <h2>Posts</h2>
            
            <br/>
    '''

    posts_end = '''
        </div>
    {% endblock %}
    '''

    posts_main = ''''''
    for item in rootPageList:
        pageName = item.split("/")[-1]
        pageNameURL = ''.join(char for char in pageName if char.isalnum())
        pageNameURL = "./posts/" + pageNameURL + ".html"

        posts_main = posts_main + '''<li><a class="link-dark rounded" href="''' + pageNameURL + '''">''' + pageName + '''</a></li>'''

    
    htmlSample = posts_start + posts_main + posts_end
    soup = BeautifulSoup(htmlSample, 'html.parser')
    return soup

def postsPageWrite():
    soup = postPageBuilder()
    template = open("./templates/posts.html",'w')
    template.write(soup.prettify())
    template.close

if __name__ == '__main__':
    postsPageWrite()

    
