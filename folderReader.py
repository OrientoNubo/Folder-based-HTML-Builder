#coding:utf-8
import os

srcPath = "./src"
treeLevel = 2

def traverseDIR():
    # Traverse the directory
    # Output array: [[first-level directory], [second-level directory], [third-level directory], ...]
    allFileList = os.walk(srcPath)
    filesNum = 0
    listLevel = []
    rootPageList = []

    for item in range(treeLevel):
        listLevel.append([])
        # listLevel = [[], [], ...]

    # print('\n', '------------------ root page list start ------------------')
    for root, dirs, files in allFileList:
        if files != []:
            rootPage = root.split("/", 2)[-1]
            # print(rootPage)
            rootPageList.append(rootPage)
            filesNum += 1
        for item in range(treeLevel):
            if (root.count("/") - 2) == item:
                name = root.split("/", 2)[-1]
                listLevel[(item)].append(name)

    # print("Total files:", filesNum)
    # print(' ------------------- root page list end -------------------', '\n')
    # print(listLevel, "\n")
    # print('\n', '------------------- ------------------- ------------------- ')
    return rootPageList, listLevel, filesNum

if __name__ == '__main__':
    traverseDIR()


