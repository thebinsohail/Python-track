
#loop count variable 
loop = int(input("Enter number of Employees: ")) 

#An empty list to store multiple input
data = [] 

#looping into the count variable
for x in range(loop): 
    data.append(input("What is the name of Employee %d ? " %(x+1))) 

#Finally printing the data
print('Following are the people in our Company\n')
print(data)
