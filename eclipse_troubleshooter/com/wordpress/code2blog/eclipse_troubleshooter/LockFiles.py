import os

# com\wordpress\code2blog\eclipse_troubleshooter
projectFolder = '../../../../'

def simple_file_read():
    fileAbsPath = os.path.abspath(projectFolder + 'resources/input.txt')
    print('file absolute path = ' + fileAbsPath)

    f = open(fileAbsPath, 'r')
    print(f.read())

def print_from_list():
    fileAbsPath = os.path.abspath(projectFolder + 'resources/input.txt')
    f = open(fileAbsPath, 'r')
    list = f.readlines()
    for index, line in enumerate(list):
        print( "line number=[{0}], {1}".format(index, line))

if __name__ == '__main__':
    print_from_list()

