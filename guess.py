import random

# 随机生成1~100整数
answer = random.randint(1, 100)
count = 0
print("====猜数字小游戏====")
print("系统已经生成1-100之间数字，请开始猜测！")

while True:
    try:
        num = int(input("请输入你猜测的数字："))
        count += 1
        if num > answer:
            print("大了")
        elif num < answer:
            print("小了")
        else:
            print(f"恭喜猜中！答案就是{answer}，你一共猜了{count}次")
            break
    except ValueError:
        print("输入错误，请输入整数！")
