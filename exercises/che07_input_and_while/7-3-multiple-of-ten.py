# 7-3 multiple of ten
for _ in range(3):
    number = int(input("Please enter a int"))
    if number % 10 == 0:
        print("Multiple of ten")
    else:
        print("Not multiple of ten")
