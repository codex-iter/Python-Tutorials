# Diving into Dictionaries

#initializing empty dictionaries

d1 = {}
print (d1) 

dict = {"name":"codex","clg":"ITER","Pass":1234}
print (dict)

# updating values in dict
print ("Before Updating: \n",dict)
dict["name"] = "codex2017"          # replace the value of key with the provided value
print("After updating: \n",dict)
del(dict["clg"])                    # deletes the value related to that key
print("After Deleting: \n",dict)    


dict = {"name":"codex","clg":"ITER","Pass":1234}

# printing dict
print (dict)         # prints the whole dictionary
print (dict["name"]) # prints the value related to the particular key