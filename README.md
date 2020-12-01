# Change Linux Files Permissions

### The purpose of this script is to facilate the process of changing files permissions
> Sometimes we just create a folder to fill it up with a bunch of scripts that we then want 
> to execute.
> Changing file permissions to those scripts can be tedius and mostly when the file system is shared with other directories

## This script iterate over a created list and make sure only files are changed. 
## Later I will add `Choosing file type functionality` 

## What this script does?
* Create a list of files out of a given directory path
* Change permissions on those files only
* Shows a string representation of those new file's permissions

## Command line arguments
#### This script accept and needs 2 command line arguments:
* path (directory path containing files)
* octal permission styles to be changed

## Accesing help menu
`$ ./change_files_permissions.py -h`

```
usage: change_files_permissions.py [-h] path perm_octal

Change files & directory permissions

positional arguments:
  path        Path where files are found. Make sure to type full directory path as /home/user/folder/ note last slash '/'
  perm_octal  Octal permissions

optional arguments:
  -h, --help  show this help message and exit
```

## Prerequisites
* Clone this repo
* Store it somewhere in your Linux system like `/opt` or `/usr/local` or `/usr/bin` if you intend to run this script from everywhere
* change script permissions to 755 `$ sudo chmod 755 change_files_permissions`

# Usage examples
`$ ./change_files_permissions.py /path/to/directory/ 755`

`$ ./change_files_permissions.py /path/to/directory/ 700`
 

*Note directory path must end with forward slash '/'*

