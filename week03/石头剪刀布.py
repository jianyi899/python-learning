# 读法：键 赢 值——石头赢剪刀，剪刀赢布，布赢石头。
import random

choices = ["石头", "剪刀", "布"]
win_map = {"石头": "剪刀", "剪刀": "布", "布": "石头"}
score = {"你": 0, "电脑": 0}
rounds = 0                    # 有效局数，自己管
while rounds < 5:
    me = input("出拳（石头/剪刀/布）：")
    if me not in choices:
        print("乱出拳！")
        continue              # 这局作废：rounds没动，等于没消耗
    rounds += 1               # 只有有效局才计数
    pc = random.choice(choices)
    # ...后面的判定照旧
# for i in range(5):       
#     me = input("出拳（石头/剪刀/布）：")
#     if me not in choices:
#         print("乱出拳！")
#         continue
#     pc = random.choice(choices)      # 新朋友：从列表里随机挑一个
    print("电脑出了：", pc)

    # 判定（提示）：
    # 1. me == pc           → 平局
    # 2. win_map[me] == pc   → 你赢，score["你"] += 1
    # 3. 否则                → 电脑赢，score["电脑"] += 1
    if me == pc:                      # 1. 出的一样 → 平局
        print("平局！")
    elif win_map[me] == pc:           # 2. 我出的键，赢的正是电脑出的值 → 你赢
        print("你赢了这局！")
        score["你"] += 1
    else:                             # 3. 其余情况 → 电脑赢
        print("电脑赢了这局！")
        score["电脑"] += 1

# 循环结束打印总比分
print("总比分 —— 你:", score["你"], "电脑:", score["电脑"])

