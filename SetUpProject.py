##############################################################
# File last modified on: 04/12/2016
# Please define the class here
##############################################################

class SetUpProject(): 

    def __init__(self): 
        self.gitignore_file = "/PythonGitIgnore/python.gitignore"


    def create_gitignore(self):
        pass

    def read_file(self, a_file_name):
        with open(a_file_name) as file:
            for line in file:
                print(line)









if __name__ == '__main__':
    f = SetUpProject()
#########################################################################################
#                                      Old Code
#########################################################################################
