# 8-9+10+11 magicians
magicians_names = [
    "Houdini",
    "David Copperfield",
    "Derren Brown",
    "Penn Jillette",
    "Teller",
    "Shin Lim",
    "Dynamo",
]


def show_magicians(names):
    for _ in names:
        print(_)


show_magicians(magicians_names)

# def make_great(names):
#    for _ in names:
#        great_names = f"the Great {_}"
#        magicians_names.append(great_names)
# 这么写把列表的长度不停地增加了，导致死循环了


def make_great(names):
    for i in range(len(names)):
        names[i] = f"the Great {names[i]}"
    print(f"\n{names}")


make_great(magicians_names[:])
show_magicians(magicians_names)
