'''
8-7 专辑 :编写一个名为make_album() 的函数，它创建一个描 述音乐专辑的字典。
这个函数应接受歌手的名字和专辑名，并返 回一个包含这两项信息的字典。使用这个函数创建三个表示不同
专辑的字典，并打印每个返回的值，以核实字典正确地存储了专 辑的信息。
'''
def make_album(singer, album, number=""):
    singer_album = {}
    singer_album[singer] = album
    singer_album['number'] = number
    return singer_album
while True:
    singer = input("Enter the name of a singer")
    if singer == 'q':
        break
    album = input("Enter the singer's album")
    if album == 'q':
        break
    amount = input("Enter the amount of songs in the album:(enter none if you do not know.)")
    if amount != 'none':
        number = int(amount)
        a = make_album(singer, album, number)
    else:
        a = make_album(singer, album)
    print(a)
'''
给函数make_album() 添加一个可选形参，以便能够存储专辑包 含的歌曲数。如果调用这个函数时指定
了歌曲数，就将这个值添 加到表示专辑的字典中。调用这个函数，并至少在一次调用中指 定专辑包含的歌曲
数
'''
