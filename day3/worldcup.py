#empty tuple initialized
worldcup=()

#take loop range
loop=int(input("Enter number of inputs to be taken: "))

#loop till the range to take inputs
for i in range(loop):
	worldcup=input("Enter value for country no %d " %(i+1) )


#display the countries
print(worldcup)