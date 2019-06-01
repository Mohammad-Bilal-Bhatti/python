# Importing system module for dealing with command line arguments.
import sys
# Importing os module for working with files
import os
# Importing shutil module for moving file form one directory to another. 
import shutil

args = len(sys.argv)
if args == 2:	# Only Source is given.
    source_dir = sys.argv[1] + os.path.sep
    dest_dir = source_dir
elif args >= 3:	# Source and Destination is given.
    source_dir = sys.argv[1] + os.path.sep
    dest_dir = sys.argv[2] + os.path.sep
else:	# In Case If No Arguments are given
	source_dir = '.'
	dest_dir = '.'

os.chdir(source_dir)
cwd = os.getcwd()

print('CWD: ',cwd)
print('Source: ',source_dir)
print('Destination: ',dest_dir)

# List all the Files and Directories present in the source directory.
files = os.listdir(source_dir)
# For each file in files.
for file in files:
    # Check weather the string is file or directory.
    if os.path.isfile(file):	# If the string is file than:
        # Find the position of the dot form the right side.
        dot = file.rfind('.')        
        # Get the extension with respect to dot.
        extension = file[dot:].lower()
        # dest_path will be destination dir + // + file_extension    e.g:  [.//.txt] or [python//file//.doc] 
        dest_path = dest_dir + os.path.sep + extension
        # Find weather the directory with that extension name is present or not?
        if os.path.exists(dest_path) == False:	# If that directory is not present than:
            # Make New Directory with that extension Name
            os.mkdir(dest_path)
        # Move the file to the respected directory.
        shutil.move(file,dest_path)
