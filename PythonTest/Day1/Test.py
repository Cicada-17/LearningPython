from random import randint

money = 1000
while money > 0:
    debt =  int(input('资金:%d   下注:' % money))
    if 0 < debt <= money :
        point = randint(1,6) + randint(1,6)
        print('玩家摇出了%d点' % point)
        if point == 7 or point == 11:
            money += debt
            print('玩家胜')
            continue
        elif point == 2 or point == 3 or point == 12:
            money -= debt
            print('庄家胜')
            continue
        else :
            while True:
                point2 = randint(1,6) + randint(1,6)
                print('玩家摇出了%d点' % point2)
                if point2 == 7 :
                    money -= debt
                    print('庄家胜')
                    break
                elif point2 == point:
                    money += debt
                    print('玩家胜')
                    break
print('你已经输光了')
