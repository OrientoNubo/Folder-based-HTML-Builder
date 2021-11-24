#coding:utf-8
import os
from folderReader import traverseDIR
from bs4 import BeautifulSoup

# <li><a href="#" class="link-dark rounded">Pages Count: ?</a></li>
# print(src)
def htmlBuilderIndex():

    src = traverseDIR()
    htmlSample = '''
    <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <style></style>
            <body></body>
        </html>
    '''

    soup = BeautifulSoup(htmlSample, 'html.parser')

    # Constitute::html:head
    headSoup = soup.head
    tag = soup.new_tag("link", rel="stylesheet", href=".{{url_for('static', filename='css/bootstrap.min.css') }}")
    headSoup.append("")
    headSoup.append(tag)
    tag = soup.new_tag("link", rel="stylesheet", href=".{{url_for('static', filename='css/sidebars.css') }}")
    headSoup.append("\n")
    headSoup.append(tag)
    tag = soup.new_tag("title")
    headSoup.append("\n")
    headSoup.append(tag)
    headSoup.title.string = "{% block title %}{% endblock %} | SHARK"
    # print(soup.head)

    # Constitute::html:style
    styleSoup = soup.style
    # print(styleSoup)

    # Constitute:::html::body:header
    headerSoup = soup.body
    header = '''<header class="d-flex justify-content-center py-3">
                    <ul class="nav nav-pills">
                        <li class="nav-item"><a href="./" class="nav-link active" aria-current="page">Home</a></li>
                        <li class="nav-item"><a href="./posts.html" class="nav-link">Posts</a></li>
                        <li class="nav-item"><a href="./caption.html" class="nav-link">Caption</a></li>
                        <li class="nav-item"><a href="./links.html" class="nav-link">Links</a></li>
                    </ul>
                </header>'''
    headerSoup.append(BeautifulSoup(header, 'html.parser'))

    # Constitute:::html::body:main
    # bodySoup = soup.body
    # tag = soup.new_tag("div")
    # soup.body.insert(0, tag)
    # tag['class'] = 'container'
    # soup.body.div.insert(0, "\n")
    mainSoup = soup.body
    main_1 = '''  <div class="container">
                    <div class="row">
                        <div class="col-md-3" id="sidebar">
                            <div class="flex-shrink-0 p-3 bg-white">
                                <a href="/" class="d-flex align-items-center pb-3 mb-3 link-dark text-decoration-none border-bottom">
                                <svg class="bi me-2" width="30" height="24"><use xlink:href="#bootstrap"></use>
                                <span class="fs-5 fw-semibold"> </span>
                                </a>'''

    # init
    main_2_sidebarVar = ''''''
    main_2_sidebarVar = main_2_sidebarVar + '<ul class="list-unstyled ps-0">'

    # main sidebar line
    for item in src[1][0]:
        # print(item)
        LEVEL_1 = item
        LEVEL_1_ID = item + "-collapse"
        LEVEL_1_ID_target = "#" + item + "-collapse"
        LEVEL_2 = ''''''

        for item2 in src[1][1]:
            item2_upper = item2.split("/")[0]
            item2_lower = item2.split("/")[1]
            # print(item)
            
            if item2_upper == item:
                # print(item, item2_upper, item2_lower)
                LEVEL_2 = LEVEL_2 + '''
                            <li><a href="./menu/''' + item2_upper + "/" + item2_lower + '''.html" class="link-dark rounded">
                            ''' + item2_lower + '''
                            </a></li>
                            '''
                # print("--------")
                ndPagePath = "./templates/menu/" + item2_upper
                isExist = os.path.exists(ndPagePath)
                if not isExist:
                    os.makedirs(ndPagePath)
                ndPageURL = "./templates/menu/" + item2_upper + "/" + item2_lower + ".html"
                temp = open(ndPageURL,'w')
                temp.close
                        
        main_2_sidebarVar = main_2_sidebarVar + '''
                                    <li class="mb-1">
                                        <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="''' + LEVEL_1_ID_target + '''" aria-expanded="false">
                                    ''' + LEVEL_1 + '''
                                        </button>
                                        <div class="collapse" id="''' + LEVEL_1_ID + '''">
                                    ''' + '''
                                        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                    ''' + LEVEL_2 + '''
                                        </ul>
                                        </div>
                                    </li>
                                    '''
    # print(main_2_sidebarVar)
    # analyze line
    main_2_sidebarVar = main_2_sidebarVar + '''
                                <li class="border-top my-3"></li>
                                <li class="mb-1">
                                    <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#account-collapse" aria-expanded="false">
                                    Analyze
                                    </button>
                                    <div class="collapse" id="account-collapse">
                                    <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                        
                                        <li><a href="#" class="link-dark rounded">Files Count: ''' + str(src[2]) + '''</a></li>
                                    </ul>
                                    </div>
                                </li>

                                </ul>'''

    main_3 = '''            </div>
                        </div>
                        <div class="col-md" id="content">
                            {% block content %}
                            {% endblock %}
                        </div>
                    </div>
                </div>'''

    main = main_1 + main_2_sidebarVar + main_3
    mainSoup.append(BeautifulSoup(main, "html.parser"))

    # Constitute:::html::body:footer
    bodySoup = soup.body
    footer = '''<div id="footer">
                    <div class="container">
                        <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                            <div class="col-md-12 d-flex align-items-center">
                                <span class="text-muted">© 2021 github.com/OrientoNubo/Folder-based-WebBuilder, repo</span>
                            </div>
                        </footer>
                    </div>
                </div>'''
    bodySoup.append(BeautifulSoup(footer, 'html.parser'))

    bodySoup = soup.body
    js ='''
                <script src=".{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
                <script src=".{{ url_for('static', filename='js/sidebars.js') }}"></script> 
            '''
    bodySoup.append(BeautifulSoup(js, 'html.parser'))

    template = open("./templates/template.html",'w')
    template.write(soup.prettify())
    template.close


def htmlBuilderPosts():

    src = traverseDIR()
    htmlSample = '''
    <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <style></style>
            <body></body>
        </html>
    '''

    soup = BeautifulSoup(htmlSample, 'html.parser')

    # Constitute::html:head
    headSoup = soup.head
    tag = soup.new_tag("link", rel="stylesheet", href="..{{url_for('static', filename='css/bootstrap.min.css') }}")
    headSoup.append("")
    headSoup.append(tag)
    tag = soup.new_tag("link", rel="stylesheet", href="..{{url_for('static', filename='css/sidebars.css') }}")
    headSoup.append("\n")
    headSoup.append(tag)
    tag = soup.new_tag("title")
    headSoup.append("\n")
    headSoup.append(tag)
    headSoup.title.string = "{% block title %}{% endblock %} | SHARK"
    # print(soup.head)

    # Constitute::html:style
    styleSoup = soup.style
    # print(styleSoup)

    # Constitute:::html::body:header
    headerSoup = soup.body
    header = '''<header class="d-flex justify-content-center py-3">
                    <ul class="nav nav-pills">
                        <li class="nav-item"><a href="../" class="nav-link active" aria-current="page">Home</a></li>
                        <li class="nav-item"><a href="../posts.html" class="nav-link">Posts</a></li>
                        <li class="nav-item"><a href="../caption.html" class="nav-link">Caption</a></li>
                        <li class="nav-item"><a href="../links.html" class="nav-link">Links</a></li>
                    </ul>
                </header>'''
    headerSoup.append(BeautifulSoup(header, 'html.parser'))

    # Constitute:::html::body:main
    # bodySoup = soup.body
    # tag = soup.new_tag("div")
    # soup.body.insert(0, tag)
    # tag['class'] = 'container'
    # soup.body.div.insert(0, "\n")
    mainSoup = soup.body
    main_1 = '''  <div class="container">
                    <div class="row">
                        <div class="col-md-3" id="sidebar">
                            <div class="flex-shrink-0 p-3 bg-white">
                                <a href="/" class="d-flex align-items-center pb-3 mb-3 link-dark text-decoration-none border-bottom">
                                <svg class="bi me-2" width="30" height="24"><use xlink:href="#bootstrap"></use>
                                <span class="fs-5 fw-semibold"> </span>
                                </a>'''

    # init
    main_2_sidebarVar = ''''''
    main_2_sidebarVar = main_2_sidebarVar + '<ul class="list-unstyled ps-0">'

    # main sidebar line
    for item in src[1][0]:
        # print(item)
        LEVEL_1 = item
        LEVEL_1_ID = item + "-collapse"
        LEVEL_1_ID_target = "#" + item + "-collapse"
        LEVEL_2 = ''''''

        for item2 in src[1][1]:
            item2_upper = item2.split("/")[0]
            item2_lower = item2.split("/")[1]
            # print(item)
            
            if item2_upper == item:
                # print(item, item2_upper, item2_lower)
                LEVEL_2 = LEVEL_2 + '''
                            <li><a href="../menu/''' + item2_upper + "/" + item2_lower + '''.html" class="link-dark rounded">
                            ''' + item2_lower + '''
                            </a></li>
                            '''
                # print("--------")
                ndPagePath = "../templates/menu/" + item2_upper
                isExist = os.path.exists(ndPagePath)
                if not isExist:
                    os.makedirs(ndPagePath)
                ndPageURL = "../templates/menu/" + item2_upper + "/" + item2_lower + ".html"
                temp = open(ndPageURL,'w')
                temp.close
                        
        main_2_sidebarVar = main_2_sidebarVar + '''
                                    <li class="mb-1">
                                        <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="''' + LEVEL_1_ID_target + '''" aria-expanded="false">
                                    ''' + LEVEL_1 + '''
                                        </button>
                                        <div class="collapse" id="''' + LEVEL_1_ID + '''">
                                    ''' + '''
                                        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                    ''' + LEVEL_2 + '''
                                        </ul>
                                        </div>
                                    </li>
                                    '''
    # print(main_2_sidebarVar)
    # analyze line

    
    main_2_sidebarVar = main_2_sidebarVar + '''
                                <li class="border-top my-3"></li>
                                <li class="mb-1">
                                    <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#account-collapse" aria-expanded="false">
                                    Analyze
                                    </button>
                                    <div class="collapse" id="account-collapse">
                                    <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                        
                                        <li><a href="#" class="link-dark rounded">Files Count: ''' + str(src[2]) + '''</a></li>
                                    </ul>
                                    </div>
                                </li>

                                </ul>'''

    main_3 = '''            </div>
                        </div>
                        <div class="col-md" id="content">
                            {% block content %}
                            {% endblock %}
                        </div>
                    </div>
                </div>'''

    main = main_1 + main_2_sidebarVar + main_3
    mainSoup.append(BeautifulSoup(main, "html.parser"))

    # Constitute:::html::body:footer
    bodySoup = soup.body
    footer = '''<div id="footer">
                    <div class="container">
                        <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                            <div class="col-md-12 d-flex align-items-center">
                                <span class="text-muted">© 2021 github.com/OrientoNubo/Folder-based-WebBuilder, repo</span>
                            </div>
                        </footer>
                    </div>
                </div>'''
    bodySoup.append(BeautifulSoup(footer, 'html.parser'))

    bodySoup = soup.body
    js ='''
                <script src="..{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
                <script src="..{{ url_for('static', filename='js/sidebars.js') }}"></script> 
            '''
    bodySoup.append(BeautifulSoup(js, 'html.parser'))

    template = open("./templates/template_posts.html",'w')
    template.write(soup.prettify())
    template.close


def htmlBuilderMenu():

    src = traverseDIR()
    htmlSample = '''
    <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <style></style>
            <body></body>
        </html>
    '''

    soup = BeautifulSoup(htmlSample, 'html.parser')

    # Constitute::html:head
    headSoup = soup.head
    tag = soup.new_tag("link", rel="stylesheet", href="../..{{url_for('static', filename='css/bootstrap.min.css') }}")
    headSoup.append("")
    headSoup.append(tag)
    tag = soup.new_tag("link", rel="stylesheet", href="../..{{url_for('static', filename='css/sidebars.css') }}")
    headSoup.append("\n")
    headSoup.append(tag)
    tag = soup.new_tag("title")
    headSoup.append("\n")
    headSoup.append(tag)
    headSoup.title.string = "{% block title %}{% endblock %} | SHARK"
    # print(soup.head)

    # Constitute::html:style
    styleSoup = soup.style
    # print(styleSoup)

    # Constitute:::html::body:header
    headerSoup = soup.body
    header = '''<header class="d-flex justify-content-center py-3">
                    <ul class="nav nav-pills">
                        <li class="nav-item"><a href="../../" class="nav-link active" aria-current="page">Home</a></li>
                        <li class="nav-item"><a href="../../posts.html" class="nav-link">Posts</a></li>
                        <li class="nav-item"><a href="../../caption.html" class="nav-link">Caption</a></li>
                        <li class="nav-item"><a href="../../links.html" class="nav-link">Links</a></li>
                    </ul>
                </header>'''
    headerSoup.append(BeautifulSoup(header, 'html.parser'))

    # Constitute:::html::body:main
    # bodySoup = soup.body
    # tag = soup.new_tag("div")
    # soup.body.insert(0, tag)
    # tag['class'] = 'container'
    # soup.body.div.insert(0, "\n")
    mainSoup = soup.body
    main_1 = '''  <div class="container">
                    <div class="row">
                        <div class="col-md-3" id="sidebar">
                            <div class="flex-shrink-0 p-3 bg-white">
                                <a href="/" class="d-flex align-items-center pb-3 mb-3 link-dark text-decoration-none border-bottom">
                                <svg class="bi me-2" width="30" height="24"><use xlink:href="#bootstrap"></use>
                                <span class="fs-5 fw-semibold"> </span>
                                </a>'''

    # init
    main_2_sidebarVar = ''''''
    main_2_sidebarVar = main_2_sidebarVar + '<ul class="list-unstyled ps-0">'

    # main sidebar line
    for item in src[1][0]:
        # print(item)
        LEVEL_1 = item
        LEVEL_1_ID = item + "-collapse"
        LEVEL_1_ID_target = "#" + item + "-collapse"
        LEVEL_2 = ''''''

        for item2 in src[1][1]:
            item2_upper = item2.split("/")[0]
            item2_lower = item2.split("/")[1]
            # print(item)
            
            if item2_upper == item:
                # print(item, item2_upper, item2_lower)
                LEVEL_2 = LEVEL_2 + '''
                            <li><a href="../../menu/''' + item2_upper + "/" + item2_lower + '''.html" class="link-dark rounded">
                            ''' + item2_lower + '''
                            </a></li>
                            '''
                # print("--------")
                ndPagePath = "../../templates/menu/" + item2_upper
                isExist = os.path.exists(ndPagePath)
                if not isExist:
                    os.makedirs(ndPagePath)
                ndPageURL = "../../templates/menu/" + item2_upper + "/" + item2_lower + ".html"
                temp = open(ndPageURL,'w')
                temp.close
                        
        main_2_sidebarVar = main_2_sidebarVar + '''
                                    <li class="mb-1">
                                        <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="''' + LEVEL_1_ID_target + '''" aria-expanded="false">
                                    ''' + LEVEL_1 + '''
                                        </button>
                                        <div class="collapse" id="''' + LEVEL_1_ID + '''">
                                    ''' + '''
                                        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                    ''' + LEVEL_2 + '''
                                        </ul>
                                        </div>
                                    </li>
                                    '''
    # print(main_2_sidebarVar)
    # analyze line
    main_2_sidebarVar = main_2_sidebarVar + '''
                                <li class="border-top my-3"></li>
                                <li class="mb-1">
                                    <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#account-collapse" aria-expanded="false">
                                    Analyze
                                    </button>
                                    <div class="collapse" id="account-collapse">
                                    <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                        
                                        <li><a href="#" class="link-dark rounded">Files Count: ''' + str(src[2]) + '''</a></li>
                                    </ul>
                                    </div>
                                </li>

                                </ul>'''

    main_3 = '''            </div>
                        </div>
                        <div class="col-md" id="content">
                            {% block content %}
                            {% endblock %}
                        </div>
                    </div>
                </div>'''

    main = main_1 + main_2_sidebarVar + main_3
    mainSoup.append(BeautifulSoup(main, "html.parser"))

    # Constitute:::html::body:footer
    bodySoup = soup.body
    footer = '''<div id="footer">
                    <div class="container">
                        <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                            <div class="col-md-12 d-flex align-items-center">
                                <span class="text-muted">© 2021 github.com/OrientoNubo/Folder-based-WebBuilder, repo</span>
                            </div>
                        </footer>
                    </div>
                </div>'''
    bodySoup.append(BeautifulSoup(footer, 'html.parser'))

    bodySoup = soup.body
    js ='''
                <script src="../..{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
                <script src="../..{{ url_for('static', filename='js/sidebars.js') }}"></script> 
            '''
    bodySoup.append(BeautifulSoup(js, 'html.parser'))

    template = open("./templates/template_menu.html",'w')
    template.write(soup.prettify())
    template.close


if __name__ == '__main__':

    htmlBuilderIndex()
    htmlBuilderPosts()
    htmlBuilderMenu()















