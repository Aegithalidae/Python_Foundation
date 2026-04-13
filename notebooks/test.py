album_info = []


def make_album(singer, album):
    return {"singer": singer, "album": album}


def gather_album(album_dic):
    album_info.append(album_dic)
    return album_info


print("\nEnter 'q' at any time to quit")
while True:
    print("\nPlease enter the singer:")
    singer = input("Singer name:")
    if singer == "q":
        break

    print("\nPlease enter the album:")
    album = input("Album name:")
    if album == "q":
        break

    album = gather_album(make_album(singer, album))
