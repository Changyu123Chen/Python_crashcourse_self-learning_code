def display_message():
	print("I have learned Function in this chapter")

display_message()


def favourite_book(person, title):
	print("One of " + person.title() + "'s favourite book is " + title.title())

favourite_book(person="Alice", title="Harry Potter")

#设置默认值
def pets(pet_name, anjmal_type="dog"):
	print("\nI have a " + anjmal_type + ".")
	print("My " + anjmal_type + "'s name is " + pet_name.title() + ".")
pets(pet_name='lala', anjmal_type='cat')

def make_shirt(size, font="I love you"):
	print("the size of the shirt is " + size.title() + " ;" + font )

make_shirt("s", "good luck!")
make_shirt("xl")

