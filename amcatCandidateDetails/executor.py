import subprocess as sub
import os

def execute(comand, directory):
    # change to the directory in which you want to execute the 		command.
    os.chdir(directory)
    p = sub.Popen(comand, stdout = sub.PIPE, stderr = sub.PIPE, shell=True)
    output, errors = p.communicate()
    # os.chdir(working_dir)
    return output, errors