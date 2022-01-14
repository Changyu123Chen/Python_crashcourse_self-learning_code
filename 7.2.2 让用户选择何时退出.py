prompt = '\nTell me something, and I will repreat it back to you: '
prompt += "\nEnter 'quit' to end the program: "
message = ' '
while message != 'quit':
	message = input(prompt)
	#加上if语句，在输入quit之后，不会返回quit
	if message != 'quit':
		print(message)

