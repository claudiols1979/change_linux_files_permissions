#!/usr/bin/env python3
import os
from os import listdir, path, walk
from os.path import isfile, join
from os import walk


def make_list_recursive(path):
    #create list of file out of directory using its path
    my_list = []
    for root, dirs, files in os.walk(path):               
        #full_path = root+'/'+dirs+'/'+files   
        #print(full_path)    
        for name in files:
            print(os.path.join(root, name))
            if isfile(join(root, name)):                        
                if name not in my_list:
                    full_path1 = root+'/'+name
                    print(full_path1)                
                    my_list.append(full_path1)
        for name in dirs:
            print(os.path.join(root, name))
            #base = os.path.split(full_path)[0]
            if isfile(join(root, name)):                        
                if name not in my_list:
                    full_path2 = root+'/'+name
                    print(full_path2)                
                    my_list.append(full_path2)                
    return my_list

new_list = make_list_recursive('/home/claudio/node')
print(new_list)