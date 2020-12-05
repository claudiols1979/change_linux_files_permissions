#!/usr/bin/env python3
import os
from os import listdir, path, walk
from os.path import isfile, join


def make_list(path):
    #create list of file out of directory using its path
    my_list = []
    for f in listdir(path):
        print(f)        
        full_path = path+'/'+f    
        print(full_path)    
        base = os.path.split(full_path)[0]
        if isfile(join(base, f)):                        
            if f not in my_list:
                print(f)                
                my_list.append(full_path)                
    return my_list

new_list = make_list('/home/claudio/change_files_permissions')
print(new_list)