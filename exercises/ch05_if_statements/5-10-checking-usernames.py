# 5-10 checking usernames
current_users = ["admin", "alice", "bob", "charlie", "david"]
current_users_lower = {user.lower() for user in current_users}
# 遇事不决先转换成小写再比较，可以避免大小写导致的用户名冲突问题。
# 新建立一个检查列表是比较好的想法
# 用集合比列表更高效，因为集合的查找时间复杂度为O(1)，而列表的查找时间复杂度为O(n)。
new_users = ["eve", "frank", "alice", "grace", "bob"]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(
            f"Sorry, the username '{new_user}' is already taken. Please choose a different username."
        )
    else:
        print(f"The username '{new_user}' is available.")
