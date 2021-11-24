#coding:utf-8
import os
from folderReader import traverseDIR
from bs4 import BeautifulSoup
import codecs

src = traverseDIR()

rootPageList = src[0]



def rootPageBuilder():
    for item in rootPageList:

        pageContent =''''''
        srcPath = "./src/" + item
        rootFilesDir = os.walk(srcPath)
        rootFiles = []
        for files in rootFilesDir:
            # print(files)
            for file in files[2]:
                Is_mp4 = file.endswith(".mp4")
                Is_flv = file.endswith(".flv")
                Is_webm = file.endswith(".webm")
                Is_ogv = file.endswith(".ogv")

                Is_mp3 = file.endswith(".mp3")

                Is_jpg = file.endswith(".jpg")
                Is_png = file.endswith(".png")

                Is_txt = file.endswith(".txt")

                if Is_mp4:
                    pageContent = pageContent + '''<h4>''' + file.split(".")[0] + '''</h4><video id="movie" preload controls width="90%" height="auto"><source src=".''' + files[0] + '''/''' + file + '''" type="video/mp4" />Your browser doesn't support this video.</video>'''
                    continue

                if Is_flv:
                    pageContent = pageContent + '''<h4>''' + file.split(".")[0] + '''</h4><video id="movie" preload controls width="90%" height="auto"><source src=".''' + files[0] + '''/''' + file + '''" type="video/mp4" />Your browser doesn't support this video.</video>'''
                    continue
                
                if Is_webm:
                    pageContent = pageContent + '''<h4>''' + file.split(".")[0] + '''</h4><video id="movie" preload controls width="90%" height="auto"><source src=".''' + files[0] + '''/''' + file + '''" type="video/web" />Your browser doesn't support this video.</video>'''
                    continue

                if Is_ogv:
                    pageContent = pageContent + '''<h4>''' + file.split(".")[0] + '''</h4><video id="movie" preload controls width="90%" height="auto"><source src=".''' + files[0] + '''/''' + file + '''" type="video/ogg" />Your browser doesn't support this video.</video>'''
                    continue

                if Is_mp3:
                    pageContent = pageContent + '''<h4>''' + file.split(".")[0] + '''</h4><audio src=".''' + files[0] + '''/''' + file + '''" autoplay controls></audio>'''
                    continue

                if Is_jpg:
                    pageContent = pageContent + '''<li>''' + file + '''</li> <img src=".''' + files[0] + '''/''' + file + '''"  width="90%" height="auto" alt="''' + file + '''"></li>'''
                    continue

                if Is_png:
                    pageContent = pageContent + '''<li>''' + file + '''</li> <img src=".''' + files[0] + '''/''' + file + '''"  width="90%" height="auto" alt="''' + file + '''"></li>'''
                    continue

                if Is_txt:
                    pageContent = pageContent + '''<h3>''' + file.split(".")[0] + '''</h3><br>'''
                    fileLink = files[0] + "/" + file
                    fi = open(fileLink, "r")
                    text = ''''''
                    for line in fi:
                        text = text + line + '''<br>''' 
                    # print(text)
                    pageContent = pageContent + text
                    continue

        pageName = item.split("/")[-1]
        pageNameMenu = item.split("/")[-2]
        pageNameURL = ''.join(char for char in pageName if char.isalnum())
        pageNameHTML = "./templates/posts/" + pageNameURL + ".html"
        
        PagePath = "./templates/posts/"
        isExist = os.path.exists(PagePath)
        if not isExist:
            os.makedirs(PagePath)

        temp = open(pageNameHTML,'w')
        htmlTemp = '''{% extends "template_posts.html" %}{% block title %}Links{% endblock %}{% block content %}<div class="jumbo"><h2>'''+ pageName +'''</h2><br/>'''+ pageContent +'''</div>{% endblock %}'''

        soup = BeautifulSoup(htmlTemp, 'html.parser')
        temp.write(soup.prettify())
        temp.close

        # print(pageNameMenu)
        # menuPath = "./templates/menu"
        # menuList = os.walk(menuPath)
        # for root, dirs, files in menuList:
        #     if files != []:
        #         for file in files:
        #             file_name = os.path.join(root,file)
        #             # print(file_name)
        #             file_name_menu = file_name.split("/")[-1].split(".")[0]
                    
                    
        #             if pageNameMenu == file_name_menu:
        #                 print(pageNameMenu, file_name_menu, "Matched!", pageName)
        #                 # print("Match!")
        #                 # print(pageNameURL)
        #                 Tempp = '''<div class="jumbo">'''+ '''<a href="../../posts/''' + pageNameURL + '''.html">'''+ pageName +'''</a>''' +'''</div>'''
        #                 # print(Temp)

        #                 f = open(file_name, 'r')
        #                 # print(f)
        #                 html_before_soup = f.read()
        #                 # print(html_before_soup)
        #                 f.close

        #                 soup = BeautifulSoup(html_before_soup, 'html.parser')
        #                 soup.append(BeautifulSoup(Tempp, 'html.parser'))
        #                 f = open(file_name, 'w')
        #                 f.write(soup.prettify())
        #                 f.close




        # print("------")
                    


if __name__ == '__main__':
    rootPageBuilder()

