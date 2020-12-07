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
        full_path = path+'/'+f        
        base = os.path.split(full_path)[0]
        if isfile(join(base, f)):                        
            if f not in my_list:                
                my_list.append(full_path)                
    return my_list

# def make_list_recursive(path):
#     #create list of file out of directory using its path
#     my_list = []
#     for root, dirs, files in os.walk(path):               
#         #full_path = root+'/'+dirs+'/'+files   
#         #print(full_path)    
#         for name in files:
#             print(os.path.join(root, name))
#             if isfile(join(root, name)):                        
#                 if name not in my_list:
#                     full_path1 = root+'/'+name
#                     print(full_path1)                
#                     my_list.append(full_path1)
#         for name in dirs:
#             print(os.path.join(root, name))
#             #base = os.path.split(full_path)[0]
#             if isfile(join(root, name)):                        
#                 if name not in my_list:
#                     full_path2 = root+'/'+name
#                     print(full_path2)                
#                     my_list.append(full_path2)                
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
    #     new_list = make_list_recursive(path)        
    #     make_exec(new_list, perm_octal)
    #     perm(new_list)
    # else:
    new_list = make_list(path)        
    make_exec(new_list, perm_octal)
    perm(new_list)    

if __name__ == "__main__":    
    import argparse

    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    #create command line arguments. "path" and "perm_octal" which is the permission in octal form
    parser = argparse.ArgumentParser(description='Change files & directory permissions')
    parser.add_argument("path", help="Path where files are found. Make sure to type full directory path as /home/user/folder/ note last slash '/'", type=str)    
    parser.add_argument('perm_octal', help="Octal permissions", type=int)
    # parser.add_argument('all', type=str2bool, nargs='?',  
    #                         const=True, default=False,
    #                         help="Change permission recursively. Possible values True or False",)
    args = parser.parse_args()
    path = args.path
    perm_octal = args.perm_octal
    # all_ = args.all
    main()