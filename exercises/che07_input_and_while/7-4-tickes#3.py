for _ in range(3):
    age = int(input("Please enter your age."))

    if age < 3:
        print("Your fee is free.")
    elif age <= 12:
        print("Your fee is $10.")
    else:
        print("Your fee is $15.")

# while True 更适合“直到某个条件发生才结束”
# for range 更适合“执行固定次数”
