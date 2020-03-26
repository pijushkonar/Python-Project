# Python-Project
## **Junk File Organizer**

### **Aim**

The aim of this project is to build a python program that runs as a command-line tool. Basically, as a lazy programmer, my desktop is full of files as shown below. Due to a large number of files, it is a daunting task to sit and organize each file. To make that task easy, we need a Python script that comes in handy and returns a folder where all the files are organized in a well-manner within seconds. It should organize by size, last used or even extensions.

### **Approach**

By using the os module of python to recursively list out all the files that are present in the folders with their relative and absolute path then create a new folder with the parent called organized which will contain all the files in organized sub-folders

### **Steps**

We import os and shutil at first.

     The OS module in python provides functions for interacting with the operating system. OS, comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.

     Shutil module in Python provides many functions of high-level operations on files and collections of files. It comes under Python’s standard utility modules. This module helps in automating the process of copying and removal of files and directories. (Ex - shutil.move() method Recursively moves a file or directory (source) to another location (destination) and returns the destination.)

Then we create the dictionaries for the folders. And the code will have the defined directories for each type of extentions 
(Example - 'Audio':('.mp3','.wav','.flac', '.m4a', '.aac') Here we define the type of extentions of files for the sub-folder Audio)

Then we start mapping the file formats with directory.



