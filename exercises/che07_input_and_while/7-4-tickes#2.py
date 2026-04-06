count = 0

while count < 3:
    age = int(input("Please enter your age."))

    if age < 3:
        print("Your fee is free.")
    elif age <= 12:
        print("Your fee is $10.")
    else:
        print("Your fee is $15.")

    count += 1

# 更进一步，固定次数的循环完全可以用for循环控制
# 详见下个单元格
