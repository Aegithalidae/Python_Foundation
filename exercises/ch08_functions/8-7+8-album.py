# 8-7+8 Album
albums = []


def make_album(singer, album_name, sing_num=""):
    if sing_num:
        return {"singer": singer, "album_name": album_name, "sing_num": sing_num}
    else:
        return {
            "singer": singer,
            "album_name": album_name,
        }


print("\nEnter 'q' at any time to quit")
while True:
    print("\nPlease enter the singer:")
    singer = input("Singer name:")
    if singer == "q":
        break

    print("\nPlease enter the album:")
    album_name = input("Album name:")
    if album_name == "q":
        break

    print("\nHow about the number of sings:")
    sing_num = input("The number(Skip if N/A):")

    album = make_album(singer, album_name, sing_num)
    albums.append(album)
print(albums)
