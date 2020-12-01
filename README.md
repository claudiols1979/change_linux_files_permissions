# Change Linux Files Permissions

### The purpose of this script is to facilate the process of changing files permissions
> Sometimes we just create a folder to fill it up with a bunch of scripts that we then want 
> to execute
> Changing file permissions to those scripts can be tedius and mostly when the file system is shared with other directories

## This script iterage over a created list and make sure only files are changed. 
## Later I will add `Choosing file type functionality` 

## What this script does?
* Create a list of files out of a given directory path
* Change permissions on those files only
* Shows a string representation of those new file's permissions

## Prerequisites
* Clone this repo
* Store it somewhere in your Linux system like `/opt` or `/usr/local` or `/usr/bin` if you intend to run this script from everywhere
* change script permissions to 755 `$ sudo chmod 755 change_files_permissions`

# Usage examples
`change_files_permissions /path/to/directory/ 755` 
`change_files_permissions /path/to/directory/ 700` 
`change_files_permissions /path/to/directory/ 750` 

*Note directory path must end with forward slash '/'*

