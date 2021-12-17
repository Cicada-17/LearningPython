    while needs_go_on:
        needs_go_on = False
        current = randint(1,6) + randint(1,6)
        print('玩家摇出%d点' % current)
        if current == 7 :
            print('庄家赢！资金：%d' % (money-debt))
            money -= debt
        elif current == first:
            print('玩家赢！资金： %d' % (money +debt))
            money += debt
        else:
            needs_go_on= True