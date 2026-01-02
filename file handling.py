
# os module:
# --------------
# ->if we want to perform any opration on file then we have to take help of os module
#
# step 1: import os
#
# method:
#
# 1. getcwd(): if you want to find the current working directory
# syntax: os.getcwd()-------------> current loc
#
# op;E:\DA\Python
# ======================================================================
# 2.chdir(): it is a method to change the directory from current working directory to specified directory
#
# ex:
#
# os.chdir(r"C:\Users\gawan\OneDrive\Desktop\aditya")
# print(os.getcwd())
#
# op: C:\Users\gawan\OneDrive\Desktop\aditya
#
# =========
# r= raw string
# =========
# ======================================================================
# 3.mkdir:
# it is used to create a directory
#
# os.chdir(r"C:\Users\gawan\OneDrive\Desktop")
# os.mkdir("test")
# here i have created a folder in desktop called test
#
# popen(): it will automatically text
# syntax:os.popen("filename.extension")
#
# ex:
# os.popen(r"C:\Users\gawan\OneDrive\Desktop\test\hii.txt")
# =======================================================================
# 4.listdir
# it is used to get all the file or folder in the form of list present in that folder
# import os
# os.chdir(r"C:\Users\gawan\OneDrive\Desktop\test")
# print(os.listdir())
#
# op:
# ['cpp.txt', 'py.txt', 'hii.txt', 'word.docx', '~$word.docx']
#
# =========================================================================
#
# 5.remove():
# it is used to remove only file from that folder
# import os
# os.chdir(r"C:\Users\gawan\OneDrive\Desktop\test")
# os.remove("hii.txt")
#
# op:
# ['cpp.txt', 'py.txt', 'word.docx', '~$word.docx']
#
# =========================================================================
#
# 6.remove()
# import os
# os.chdir(r"C:\Users\gawan\OneDrive\Desktop")
# os.rmdir("aditya")
#
# here i have removed the aditya folder from desktop
#
# *************************************************************************************************************
# note: if you want to remove a folder that folder must be empty if its having some file then we will get an error
# *************************************************************************************************************
#
# ===============================================================================
#
# 7.rename
# ----------------
# it is used to rename both file as well as folder
#
# import os
# os.chdir(r"C:\Users\gawan\OneDrive\Desktop")
# os.rename("ok.txt","k.txt")
# os.rename("a","b")
#
# ==================================================================================
#
# in file handling there are two types
#         1.text file
#         2.binary file
#
# #without content manager
# --------------------------------------
# here we cannot close file automatically
#
# new_var=open('filename.exe','mode')
#
# in mode we have 4 types
#         1.'r'=read
#         2.write='w'
#         3.append='a'
#         4.create='x'
# here in x we cant do any operation
#
# with content manager:
# ------------------------------
# here we can close file automatically
#
# with open('filename.extension','mode') as object;
#         pass/......

# ex:

# import os
# os.chdir(r"C:\Users\gawan\OneDrive\Desktop\b")
# print(os.getcwd())
# file=open("abc.txt","x")
# os.popen('abc.txt')
#
#
#


import os
os.chdir(r"C:\Users\gawan\OneDrive\Desktop\b")
# print(os.getcwd())
file=open("abc.txt",)
