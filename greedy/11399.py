numOfMan = int(input())
drawTimeList = [int(i) for i in input().split(" ")]
drawTimeList.sort()
drawTimePerMan = 0
totalDrawTime = 0
for i in drawTimeList:
    drawTimePerMan = drawTimePerMan + i
    totalDrawTime += drawTimePerMan
print(totalDrawTime)
