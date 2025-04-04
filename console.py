import random

choices = ['石头','布','剪刀']

player = input('请出拳：(输入"退出"以退出):')
while (player != '退出'):
    computer = random.choice(choices)
    if (player == computer) :
        print((((('你出了' + player) + '，电脑出了') + computer) + '...'))
        print("平局！")
    elif (player == '石头') :
        print((((('你出了' + player) + '，电脑出了') + computer) + '...'))
        if computer == "剪刀":
            print("你赢了！")
        else:
            print("电脑赢了！")
    elif (player == '布') :
        print((((('你出了' + player) + '，电脑出了') + computer) + '...'))
        if computer == "石头":
            print("你赢了")
        else:
            print("电脑赢了！")
    elif (player == '剪刀') :
        print((((('你出了' + player) + '，电脑出了') + computer) + '...'))
        if computer == "布":
            print("你赢了")
        else:
            print("电脑赢了！")
    else :
        print("输入错误：只能输入“石头”“剪刀”或“布”")
    player = input('请出拳:(输入"退出"以退出):')
