# diving into loops

# for loop:

#In the loop below, the range of x will be from 1 to 10 . The value will start from 1 and continue 9
for x in range(1,10):
    print(x)

print("\n\n")

# In the loop below the value will start from 1 and will continue to 10 but the after each iteration the value will be increased by 2
for x in range(1,10,2):
    print(x)

print("\n\n")

# Traversing a list using for loop:
list = [10 ,20 ,30 ,40 ,50]
for i in list:
    print(i)




# while loop:

i = 10

while (i > 0):
    print (i)
    i-=1