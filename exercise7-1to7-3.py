car = input("Tell me what car do you want to rent? ")
print("Let me see if I can find you a " + car)

ren = input("how many people")
ren = int(ren)
if ren>8:
	print("no table")
else:
	print("come")

number = input("enter a number")
number = int(number)
if number % 10 == 0:
	print("10 beishu")
else:
	print("no")