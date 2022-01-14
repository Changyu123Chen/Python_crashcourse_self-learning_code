def greet_user():
	print("Hello!")
greet_user()

def greet_user(username): #此处的username是一个形参
	print("Hello, " + username.title() + "!")
greet_user("jesse") #这里的jesse是一个实参