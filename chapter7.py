message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("\nHello, " + name + "!" )

prompt = "If you tell us who you are, we can personalize the messages you see. "
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

age = input("Please enter your age: ")
age = int(age)
if age > 18:
	print("You can vote")
else:
	print("You are too young to vote.")