##############################################################
# File last modified on: 04/12/2016
# Please define the class here
##############################################################
from io import TextIOWrapper

class CreateGitIgnore():

    def __init__(self): 
        self.gitignore_file = "/Users/Nic/PersonalProjects/SupportClasses/PythonGitIgnore/python.gitingore"
        self.file_name = ".gitingore"


    def create_gitignore(self):
        pass

    def read_file(self):
        with open(self.gitignore_file, 'r') as file:
            for line in file:
                self.write_file(line)

    def write_file(self, line):
        with open(self.file_name, 'a') as file:
            file.write(line)

if __name__ == '__main__':
    f = CreateGitIgnore()
    f.read_file()
#########################################################################################
#                                      Old Code
#########################################################################################
