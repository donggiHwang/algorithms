numOfCoin, total = map(int, input().split(" "))
result = 0
coin = []
for i in range(0, numOfCoin):
    coin.append(int(input()))
while len(coin) > 0:
    c = coin.pop()
    result += total // c
    total %= c
print(result)