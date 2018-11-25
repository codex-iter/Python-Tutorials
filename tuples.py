#Diving into tuples

#initializing empty tuples
t1 = ()
print (t1)

t2 = (1,2,3,4,5)                    # tuple with number datatype
t3 = ("codex" , "iter" , "python")  # tuple with string datatype
t4 = ("codex" , 25 , 50.25 , "iter") # tuple with different datatype

print (t2)
print (t3)
print (t4)


tupple = (10 , 20 , 30 , 40 , 50)
# printing tuples
print (tupple)         #prints the whole tuples
print (tupple[2])      #prints the 2nd index ,i.e, the 3rd element of the tuples
print (tupple[1:3])    #prints the tuple value from 2nd value to 4th
print (tupple[::-1])   #prints the tuple in reverse order
print (tupple[-1])     #prints the last element when the index goes -ve. it will go from backward


# IMPORTANT:
# Changing values in tuple is not allowed
# Deleting a single element is not allowed. you have to delete the whole tuple
