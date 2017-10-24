# Diving into file handling

# This will help in reading, writting, appending a file.

'''
 Syntax:
 
file_object_variable_name = open("file_name" , "access_mode")

file_object_variable_name : This the variable name you want to give through which you can do operations on the file.
file_name: The name of the file you want to edit/read
access_mode : the mode in which you want to open the file. The basic modes are:
    r  : Opens a file for reading only.
    w  : Opens a file for writing only.
    a  : Opens a file for appending.
    a+ : Opens a file for both appending and reading.
    r+ : Opens a file for both reading and writing. 
    w+ : Opens a file for both writing and reading.

 '''

# This will open in read mode but you can't do any edits.
fp = open("demotext.txt","r")
x = fp.read()      # It will read the whole file and save all in a single string
print(x)
fp.close()

fp = open("demotext.txt","r")
y = fp.readline()      # It will read the first line of the file and store it in a string
print(y)
fp.close()

fp = open("demotext.txt","r")
z = fp.readlines()      # It will read the whole file and store the whole in in a list with each line as a sinlge value
print(z)
fp.close()

# This will open the file in append mode.
fp = open("demotext.txt","a")
fp.write("Text appended")
fp.close()
fp = open("demotext.txt","r")
x = fp.read()
print(x)
fp.close()

# This will open the file in write mode
fp = open("demotext.txt","w")
fp.write("Opened in write mode. so, all text gone")
fp.close()
fp = open("demotext.txt","r")
x = fp.read()
print(x)
fp.close()


# This will open the file in both append and read mode
fp = open("demotext.txt","a+")
x = fp.read()
print(x)
fp.write("Text Appended.\n CODEX ITER")
fp.close()

print(fp.closed)    # This will return a boolean value for the status of file closed or not
print(fp.mode)      # This will return the value in which the file is opened
