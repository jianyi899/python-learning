# 1. 电脑随机出一个 1-100 的数（提示：import random）
# 2. 死循环：让玩家输入一个数（提示：input() 要转成整数）
# 3. 猜大了提示"大了"，猜小了提示"小了"
# 4. 猜中了：恭喜 + 跳出循环
import random

num = random.randint(1, 100)
while True:
    guess = int(input("请输入你猜得数："))
    if guess > num:
        print("猜大了")
        continue
    elif guess < num:
        print("猜小了")
        continue
    else:
        print("恭喜猜对了")
        break

