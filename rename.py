import os
import sys

directoryWhiteList = [".git"]
fileWhiteList = ["rename.py"]




def getNewName(oldName):
    newName = ""
    outputFlag = True
    for tmpChar in oldName:
        if tmpChar == "[":
            outputFlag = False
        elif tmpChar == "]":
            outputFlag = True
        elif outputFlag:
            newName += tmpChar
    return newName

def getDirectoryList(dirPath):
    dirList = []
    allList = os.listdir(dirPath)
    for i in allList:
        if os.path.isdir(i) and not i in directoryWhiteList:
            dirList.append(i)
    return dirList

def getFileList(dirPath):
    fileList = []
    allList = os.listdir(dirPath)
    for i in allList:
        if os.path.isfile(i) and not i in fileWhiteList:
            fileList.append(i)
    return fileList


if len(sys.argv)<2:
    print("No input!")
    exit()

inputDir = sys.argv[1]


if not os.path.isdir(inputDir):

fileList = getFileList(inputDir)
print(fileWhiteList)