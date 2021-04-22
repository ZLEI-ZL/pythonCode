from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(n, winsA, winsB)

def printIntro():
    print("该程序模拟乒乓球运动员比赛")

def getInputs():
    a = eval(input("请输入A选手能力值（0-1）："))
    b = eval(input("请输入B选手能力值（0-1）："))
    n = eval(input("请输入模拟比赛场次："))

    return a, b, n

def simNGames(n, probA, probB):
    winsA, winsB = 0, 0

    for i in range(n):

        scoreA, scoreB = simOneGame(probA, probB)

        if scoreA > scoreB:

            winsA += 1

        else:

            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):

    scoreA, scoreB = 0, 0

    serving = "A"

    while not gameOver(scoreA, scoreB):

        if serving == "A":

            if random() < probA:
                scoreA += 1

            else:
                serving = "B"

        else:

            if random() < probB:
                scoreB += 1

            else:
                serving = "A"

    return scoreA, scoreB

def gameOver(a, b):

    return a == 11 or b == 11

def printSummary(n, winsA, winsB):

    print("比赛共进行{}场".format(n))
    print("A选手获胜{}场，占比{:0.1%}".format(winsA, winsA/n))
    print("B选手获胜{}场，占比{:0.1%}".format(winsB, winsB/n))

main()