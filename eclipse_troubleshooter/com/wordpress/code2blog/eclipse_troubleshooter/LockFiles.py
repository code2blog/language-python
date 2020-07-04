import os
# com\wordpress\code2blog\eclipse_troubleshooter
projectFolder = '../../../../'
fileAbsPath = os.path.abspath(projectFolder + 'resources/input.txt')
print('file absolute path = ' + fileAbsPath)

f = open(fileAbsPath, 'r')
print(f.read())
