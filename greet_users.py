#greet_users.py
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['Alice','peter','jack']
greet_users(usernames)
