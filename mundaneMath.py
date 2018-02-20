# Mingjie Zhao
# Adds together all the even numbers between 1 and 100, 
# and prints to the terminal.

sum = 0

for i in range(101):
	if i % 2 == 0:
		sum = sum + i

print (sum)

