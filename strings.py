# Diving into string type data type
name = "CODEX"
print (name)            # prints the whole string
print (name[1])         # prints the character os specific index, here "O"
print (name[1:3])       # prints the string from 1st index to 3rd i.e, 2nd character to 4th
print (name[1:])        # prints the whole string from 1st index i.e, 2nd character to last
print (name*2)          # prints the string 2 times
print (name + " ITER")  # prints the string along with the added string
print (name[::-1])      # prints the string in reversed order
print ("The String is",name,"ITER") #printing the string along with other string

# printing sentences
# '\t' : to give tabs
# '\n' : next line
long_string = "\n\nLorem \t ipsum \t dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print (long_string)

#another way to write long paragraphs in multi line
long_string = """\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n"""
print (long_string)


# some other useful built-in string methods
print (name.capitalize())  # capitalizes first letter of string
print (name.upper())       # converts all lowercase letters in string to uppercase
print (name.lower())       # converts all uppercase letters in string to lowercase
print (len(name))         # prints the length of the string

