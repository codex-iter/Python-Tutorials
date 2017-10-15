# Diving into lists

#initializing a empty list
l1 = []
print (l1)

l2 = [1,2,3,4,5]                    # list with number datatype
l3 = ["codex" , "iter" , "python"]  # list with string datatype
l4 = ["codex" , 25 , 50.25 , "iter"] # list with different datatype

print (l2)
print (l3)
print (l4)


# updating value of lists
list = [10 , 20 , 30 , 40 , 50]
print ("Before Updation: \n",list)
list[2] = 100       # the 2nd index i.e, 3rd element of the list will beupdated to 100
print ("After updation: \n",list)
del( list[2])       #deletes the 2nd index, i.e, the 3rd element of the list
print("After deleting: \n",list)
list.append(60)     #add the value 60 at the end of the list
print("After appending list:\n",list)


# printing lists
print (list)         #prints the whole list
print (list[2])      #prints the 2nd index ,i.e, the 3rd element of the list
print (list[1:3])    #prints the list value from 2nd value to 4th
print (list[::-1])   #prints the list in reverse order
print (list[-1])     #prints the last element when the index goes -ve. it will go from backward

