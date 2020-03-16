broken, numOfBrand = [int(i) for i in input().split(" ")]
minPerLine = 1000
minPerPack = 1000
for i in range(0, numOfBrand):
    price = [int(i) for i in input().split(" ")]
    minPerPack = min(minPerPack, price[0])
    minPerLine = min(minPerLine, price[1])
totalPrice = 0
while broken >= 0:
    if broken < 6:
        totalPrice = totalPrice + (minPerLine * broken) if minPerPack > (minPerLine * broken) else totalPrice + minPerPack
        break
    elif minPerPack < (minPerLine * 6):
        totalPrice = totalPrice + minPerPack
        broken -= 6
    else:
        totalPrice = totalPrice + (minPerLine * 6)
        broken -= 6
print(totalPrice)