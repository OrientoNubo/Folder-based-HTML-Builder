#coding:utf-8
import os
import sys
import urllib
from flask import Flask
import urllib
from folderReader import traverseDIR

def appBuilder():
    src = traverseDIR()
    app = "./app.py"
    temp = open(app,'w')

    appMain = '''#coding:utf-8
import os
from flask import Flask, render_template
from folderReader import traverseDIR

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/posts.html')
def posts():
    return render_template('posts.html')

@app.route('/caption.html')
def caption():
    return render_template('caption.html')

@app.route('/links.html')
def links():
    return render_template('links.html')

    '''

    menuList = []
    for item in src[0]:
        if item.split("/")[1] not in menuList:
            menuList.append(item.split("/")[1])
            # print(menuList)
            menuNAME = item.split("/")[1]

            appAdd = '''
@app.route('/menu/''' + item.split("/")[0] + "/" + item.split("/")[1] + '''.html')
def ''' + menuNAME + '''():
    return render_template("/menu/''' + item.split("/")[0] + "/" + item.split("/")[1] + '''.html")

    '''
            appMain = appMain + appAdd



    for item in src[0]:
        pageName = item.split("/")[-1]
        # pageNameURL = urllib.parse.quote(pageName.encode(sys.stdin.encoding).decode('utf8'))
        pageNameURL = ''.join(char for char in pageName if char.isalnum())
        appAdd = '''
@app.route('/posts/''' + pageNameURL + '''.html')
def ''' + pageNameURL + '''():
    return render_template("/posts/''' + pageNameURL + '''.html")

    '''
        appMain = appMain + appAdd

    appMain = appMain + '''

if __name__ == '__main__':
    app.run(debug=True)
        '''

    temp.write(appMain)
    temp.close

if __name__ == '__main__':
    appBuilder()