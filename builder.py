#coding:utf-8
import os
import sys
import shutil
from folderReader import traverseDIR
from templateBuilder import htmlBuilderIndex, htmlBuilderPosts, htmlBuilderMenu
from rootPageBuilder import rootPageBuilder
from staticPageBuilder import StaticPageBuilder
from postPageBuilder import postsPageWrite
from labelMenu import menuPreWrite
from appBuilder import appBuilder

def removeExpired(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        pass
        # print("Error: %s - %s." % (e.filename, e.strerror))

def removeFile(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        pass

def mkdir(tempPath):
    Path = "./templates/posts/"
    isExist = os.path.exists(tempPath)
    if not isExist:
        os.makedirs(tempPath)



if __name__ == '__main__':

    file_path = "./app.py"
    removeFile(file_path)

    tempPath = "./templates"
    removeExpired(tempPath)
    mkdir(tempPath)
    
    StaticList = ['Home', 'Caption', 'Links']
    StaticPageBuilder(StaticList)

    htmlBuilderIndex()

    htmlBuilderPosts()

    htmlBuilderMenu()

    rootPageBuilder()

    postsPageWrite()

    menuPreWrite()

    appBuilder()



