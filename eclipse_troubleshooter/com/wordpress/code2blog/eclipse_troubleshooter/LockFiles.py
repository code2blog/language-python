import os
import re

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
        print("line number=[{0}], {1}".format(index, line))


def find_lock_files():
    fileAbsPath = os.path.abspath(projectFolder + 'resources/lock_file_paths.txt')
    f = open(fileAbsPath, 'r')
    list = f.readlines()
    for index, line in enumerate(list):
        # sanitize input passed in through config file - lock_file_paths.txt
        line = line.strip()
        if(not line.endswith('/') and not line.endswith("\\")):
            line = line + '/'
        #
        # print("line {0} from config file = {1}".format(index, line))
        lock_files = [any_file for any_file in os.listdir(line) if re.match(r'.*Lock', any_file)]
        for file in lock_files:
            abs_lock_file = line + file
            print("lock file found : {0}".format(abs_lock_file[-100:]))

if __name__ == '__main__':
    find_lock_files()
