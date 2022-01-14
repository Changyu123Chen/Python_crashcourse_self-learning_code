def show_magicians(magic):

    for magician in magic:
        print(magician.title())



def make_great(magi):
    a = magi[:]
    magi = ["the great " + s for s in magi]
    print(magi)
    print(a)

magicians = ['avd', 'dc', 'sds', 'sssdw']
show_magicians(magicians)
make_great(magicians)
