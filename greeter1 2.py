def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
while True:
	print("\nPlease tell me your name: ")
	f_name = input("First name: \n(enter 'q' at any time to quit)")
	if f_name =='q':
		break
	l_name = input("Last_name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

