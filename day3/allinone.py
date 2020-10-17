#tuples in Python

data=("Anas","Addu","Ali","Eclipse");

print(data[0])

##################################################################

#Ranges in Tuples

let=("Java","C","R","Python")

# Printing all the elements from index 2 to last index 
print(let[2:])

# let[-2] is R here 
print(let[-2])

#Whenver you write in terms of negative value it means starting from the last index for example 
#-1 is the last index aka Python in let dataset

#################################################################


#empty tuple initialized
worldcup=()

#take loop range
loop=int(input("Enter number of inputs to be taken: "))

#loop till the range to take inputs
for i in range(loop):
	worldcup=input("Enter value for country no %d " %(i+1) )


#display the countries
print(worldcup)