import random

levels = {"简单": 20, "普通": 50, "困难": 100}
records = []                     # 每局猜的次数，都存这里

while True:                      # 外层循环：一局接一局玩
    choice = input("选难度（简单/普通/困难）：")
    choice = choice.strip()

    if choice in levels:
        limit = levels[choice]
    else:
        print("没有这个难度，请重新输入")
        continue
    # limit = ???                  # 提示：从字典里按 choice 取上限

    answer = random.randint(1, limit)
    count = 0                    # 本局猜了几次

    while True:                  # 内层循环：本局猜数
        guess = input("猜一个1到"+str(limit)+"的整数：")
        guess = guess.strip()
        if not guess.isdigit():
            print("要输入数字哦，再试一次。")
            continue
        guess = int(guess)
        count = count + 1
        # 大了/小了/猜中的判断——你v1里写过，直接搬
        # 猜中时：把 count 塞进 records，然后 break
        if guess > answer:
            print("大了")
        elif guess<answer:
            print("小了")
        else:
            print("猜中！答案是",answer,",你用了",count,"次。")
            records.append(count)
            break
             


    again = input("再来一局？(y/n)：")
    again = again.strip().lower()
    if again != "y":                      # 不是y就跳出外层循环
        break

print("共玩了", len(records), "局")
if len(records)>0:
    total =sum(records)
    average = total / len(records)
else:
    print("一局都没玩，下次再来。")    

print("平均每次猜中用了", average, "次")
