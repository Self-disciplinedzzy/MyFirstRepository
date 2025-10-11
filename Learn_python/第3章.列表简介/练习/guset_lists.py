guest_list = ["xiaoyan", "chenpinan", "luofeng", "wangling", "yefan"]
message = f"Welcome {guest_list[0].title()}, {
    guest_list[1].title()}... to my party. "
print(message)

print(f"My frend {guest_list[0].title()} cannot to my party.")
guest_list[0] = "limuwan"

message = f"Welcome {guest_list[0].title()}, {
    guest_list[1].title()}...to my party."
print(message)

print("我找到一个更大餐桌")
guest_list.insert(0, "xiaoyan")
guest_list.insert(2, "cailing")
guest_list.append("xuxin")
message = f"Welcome {guest_list[0].title()}, {guest_list[1].title()}, {
    guest_list[2]}... to my party. "
print(message)
print(guest_list)
message = f"我只能和{guest_list[0].title()} and {guest_list[2].title()}共进晚餐."
guest_list.pop(1)
guest_list.pop(-1)
guest_list.pop(-1)
guest_list.pop(-1)
guest_list.pop(-1)
guest_list.pop(-1)
print(guest_list)
del guest_list[0]
del guest_list[0]
print(guest_list)
print(len(guest_list))
# 有意引发错误
# print(guest_list[-1])
