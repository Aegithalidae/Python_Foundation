# 7-5 tickets
count = 0

while True:
    age = int(input("Please enter your age."))
    if age < 3:
        if count < 3:
            print("Your fee is free.")
            count += 1
        else:
            break
    elif age <= 12:
        if count < 3:
            print("Your fee is $10.")
            count += 1
        else:
            break
    elif age > 12:
        if count < 3:
            print("Your fee is $15.")
            count += 1
        else:
            break

# 这份代码写的很垃圾，控制循环的逻辑不应该写在if分支里
# 一个比较自然的顺序是
# 先判断是否能继续输入
# 再获取输入
# 根据输入决定输出
# 优化代码见下一个单元格
