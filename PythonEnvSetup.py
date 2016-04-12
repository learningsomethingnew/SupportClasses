##############################################################
# File last modified on: 04/12/2016
# Runs bash commands for setting up a python env.
# Subprocess.run() is what is used to execute said bash commands.
##############################################################
import subprocess

class PythonEnvSetup(): 

    def __init__(self): 
        pass

    def main(self):
        subprocess.run(["echo layout python3 > .envrc"])
        subprocess.run(["direnv", "allow"])
        subprocess.run(["which", "python"])


if __name__ == '__main__':
    f = PythonEnvSetup()
    f.main()
#########################################################################################
#                                      Old Code
#########################################################################################
