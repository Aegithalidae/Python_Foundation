# 5-9 no users
users = ["admin", "alice", "bob", "charlie", "david"]

for user in users:
    del users[0]
    if users:
        print("We have some users!")
    else:
        print("We need to find some users!")
print(users)
# 注意，在循环中删除列表元素可能会导致意外行为，因为列表的长度在迭代过程中发生变化。
# 在这个例子中，循环会删除列表中的元素，但由于列表长度在迭代过程中发生变化，可能会导致某些元素被跳过或引发错误。
# 更安全的做法是在循环外部检查列表是否为空，而不是在循环内部删除元素。
# 这个例子中，第一次循环时，会删除'admin'并打印"We have some users!"
# 但注意，第二次循环开始时，迭代器索引从0指向1，此时列表的索引1并不是原来的'alice'，而是'bob'
# 因此，'alice'会被跳过，导致输出结果不正确。
# 同理，第三次循环时，索引指向2，此时列表的索引2是'david'，而不是'charlie'，导致'charlie'也被跳过。
# 最后一次循环时，索引指向3，此时列表的索引3已经不存在，会退出遍历。
# 因此，users的元素还剩下['charlie', 'david']，而不是被完全清空。


# 5-9 no users
users = ["admin", "alice", "bob", "charlie", "david"]

while users:
    users.pop()
    if users:
        print("We have some users!")
    else:
        print("We need to find some users!")
print(users)
# 这个例子中，使用while循环和pop方法来逐个删除列表中的元素，直到列表为空。
# 每次循环时，pop方法会删除列表中的最后一个元素，并返回该元素的值。
# 当列表不为空时，打印"We have some users!"；当列表为空时，打印"We need to find some users!"。
# 最后，打印空列表[]，表示所有用户都已被删除。
# 相比遍历同时删除元素的方式，这种方法更安全，不会导致跳过元素或引发错误。
