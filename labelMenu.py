#coding:utf-8
import os
from folderReader import traverseDIR
from bs4 import BeautifulSoup


def menuRead(menuFileList):
    menuPath = "./templates/menu"
    menuList = os.walk(menuPath)
    for root, dirs, files in menuList:
        if files != []:
            for file in files:
                file_name = os.path.join(root,file)
                menuFileList.append(file_name)
    return menuFileList

def postsRead(postsFileList):
    postsPath = "./src"
    postsList = os.walk(postsPath)
    for root, dirs, files in postsList:
        if root != []:
            # print(root, root.count("/"))
            if root.count("/") >= 4:
                postsFileList.append(root.split("/", 3)[-1])
    return postsFileList


def menuPreWrite():
    menuFileList_init = []
    menuFileList = menuRead(menuFileList_init)
    # print(menuFileList)

    postsFileList_init = []
    postsFileList = postsRead(postsFileList_init)
    # print(postsFileList)


    for item in menuFileList:
        # print(item)

        ContentUpper = '''{% extends "template_menu.html" %}{% block title %}Links{% endblock %}{% block content %}<div class="jumbo"><h2>Links</h2><br/>'''

        Contentlower = '''</div>{% endblock %}'''
    
        ContentMain = ''''''

        for Postsitem in postsFileList:
            if (item.split("/", -1)[-1]).split(".", -1)[0] == (Postsitem.split("/", -1)[0]):
                postName = Postsitem.split("/", -1)[-1]
                postNameUni = ''.join(char for char in postName if char.isalnum())
                ContentPost = '''<li><a href="../../posts/''' + postNameUni + '''.html">''' + postName + '''</a></li><br>'''
                ContentMain = ContentMain + ContentPost


        Content = ContentUpper + ContentMain + Contentlower

        HTML = open(item, 'r')
        HTML_Content = HTML.read()
        HTML.close
        soup = BeautifulSoup(HTML_Content, 'html.parser')
        soup.append(BeautifulSoup(Content, 'html.parser'))
        HTML = open(item, 'w')
        HTML.write(soup.prettify())
        HTML.close



if __name__ == '__main__':

    menuPreWrite()
