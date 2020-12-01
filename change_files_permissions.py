#!/usr/bin/python3
from os import listdir
from os.path import isfile, join
import subprocess
import sys
import os
from stat import ST_MODE
"""
This script creates a list of files out of a given path and turn it into a list. This is is iterated and if an object is a file then
permissions are set and return a print statement new new permissions assigned
"""
# needs to implete os.walk in order to get access recursively to all files in a tree
def make_list(path):
    #create list of file out of directory using its path
    my_list = []
    for f in listdir(path):        
        full_path = path+f        
        base = os.path.split(full_path)[0]
        if isfile(join(base, f)):                        
            if f not in my_list:                
                my_list.append(full_path)                
    return my_list

# def make_list_all(path):
#     my_list = []
#     for f in listdir(path):
#         full_path = path+f                           
#         if f not in my_list:                
#             my_list.append(full_path)
#             print(my_list)                
#     return my_list

def make_exec(list, perm_octal):
    # iterate over the list and change file permissions as requested
    command = 'sudo'
    arg1 =  'chmod'
    perm_octal = sys.argv[2]    
    for i in list:
        if i != "make_file_list.py":
            arg3 = i
            subprocess.call([command, arg1, perm_octal, arg3])        
    return list

def perm(list):
    #print a string representation of the new file permissions    
    for i in list:        
        octal = oct(os.stat(i)[ST_MODE])[-3:]
        res = print("{:<95} has now the following permissions *{}*".format(i, octal))
    return res

def main():
    # if sys.argv[3] == True:
    #     new_list = make_list_all(path)        
    #     make_exec(new_list, perm_octal)
    #     perm(new_list)
    # else:
    new_list = make_list(path)        
    make_exec(new_list, perm_octal)
    perm(new_list)    

if __name__ == "__main__":    
    import argparse
    #create command line arguments. "path" and "perm_octal" which is the permission in octal form
    parser = argparse.ArgumentParser(description='Change files & directory permissions')
    parser.add_argument("path", help="Path where files are found. Make sure to type full directory path as /home/user/folder/ note last slash '/'", type=str)    
    parser.add_argument('perm_octal', help="Octal permissions", type=int)
    #parser.add_argument('all', help="Change permission of directories as well. Possible values True or False", type=bool)
    args = parser.parse_args()
    path = args.path
    perm_octal = args.perm_octal
    #all = args.all   
    main()