from random import random
from socket import if_nameindex
def printIntro():
    print("这个程序模拟A,B两个选手的比赛：\n")
    print("这个程序的实现需要知道A，B两个选手的能力值，该值为0-1之间的小数：\n")
printIntro()
def getInputs():
    probA = eval(input("请输入A的能力值："))
    probB = eval(input("请输入B的能力值："))
    n=int(input("请输入比赛场次："))
    return probA,probB,n
def printSummary(winsA,winsB):
    print("预计A会赢得{}场比赛".format(winsA))
    print("预计B会赢得{}场比赛".format(winsB))
def simNGames(probA,probB,n):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOneGame(probA,probB)
        if(scoreA>scoreB):
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB
def simOneGame(probA,probB):
    scoreA,scoreB=0,0
    serve='A'
    while not onegameOver(scoreA,scoreB):
        if (serve=='A'):
            if(random()<=probA):
                scoreA += 1
            else:
                serve='B'
        if (serve=='B'):
            if(random()<=probB):
                scoreB += 1
            else:
                serve='A'
    return scoreA,scoreB
def onegameOver(a,b):
    return a==15 or b==15
def game_main():
    probA,probB,n=getInputs()
    winsA,winsB=simNGames(probA,probB,n)
    printSummary(winsA,winsB)
if  __name__ =='_main_':
    game_main()

