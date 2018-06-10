# Its will import os module in the python and load required function in the library for that.
import os

# This will return current working directory of the system. The exact location of your working directory
wd = os.getcwd()

# the value of the wd is same as the path of the current working directory in the string format
# If we pass the value of the current working directory it [listdir] will return the list of directory 
# as we pass in the system.
os.listdir(wd)
