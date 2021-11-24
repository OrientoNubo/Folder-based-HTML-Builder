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

    removeFile("./app.py")
    removeFile("./src/__init__.py")
    removeExpired("./templates")
    mkdir("./templates")
    
    StaticList = ['Home', 'Caption', 'Links']
    StaticPageBuilder(StaticList)

    htmlBuilderIndex()

    htmlBuilderPosts()

    htmlBuilderMenu()

    rootPageBuilder()

    postsPageWrite()

    menuPreWrite()

    appBuilder()



