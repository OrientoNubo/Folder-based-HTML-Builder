#coding:utf-8
import os
from bs4 import BeautifulSoup

def StaticPageBuilder(StaticList):
    for item in StaticList:
        Path = "./templates/" + item.lower() + ".html"
        
        # Home
        htmlContent = '''{% extends "template.html" %}
                            {% block title %}

                            ''' + item + '''

                            {% endblock %}
                            {% block content %}

                            <h2>''' + item + '''</h2>
            
                            Lorem est eu officia consectetur elit tempor officia id sit nisi cupidatat. Non tempor proident qui cupidatat duis velit aute nostrud aliqua minim proident laboris. Ipsum est tempor eu voluptate nostrud aliquip consectetur. Lorem eiusmod culpa amet adipisicing tempor fugiat est commodo reprehenderit exercitation adipisicing. Sunt incididunt duis ipsum qui do amet do amet. Aliquip magna nisi fugiat labore et nisi magna mollit aliquip sunt. Nisi quis pariatur reprehenderit sint sint irure esse nostrud.

                            {% endblock %}'''
        file = open(Path, 'w')
        soup = BeautifulSoup(htmlContent, 'html.parser')
        file.write(soup.prettify())
        file.close



if __name__ == '__main__':
    StaticList = ['Home', 'Caption', 'Links']
    StaticPageBuilder(StaticList)