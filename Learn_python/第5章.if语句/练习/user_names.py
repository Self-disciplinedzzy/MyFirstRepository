current_users = ['wuqibo', 'zhangzhenpin', 'zhoutao',
                 'xianghaowen', 'lizhiping']
new_users = ['zhouzhijie', 'wangyanan', 'wuqibo',
             'wanghaibin', 'xianghaowen']
for new_user in new_users:
    if new_user in current_users:
        print("这个用户名已被使用")
    else:
        print("这个用户名未被使用")
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())
print(current_users_lower)
