numOfHouse = int(input())
price = [0, 0, 0]
for i in range(0, numOfHouse):
    nr, ng, nb = map(int, input().split(" "))
    pr, pg, pb = price
    price[0] = min(pg + nr, pb + nr)
    price[1] = min(pr + ng, pb + ng)
    price[2] = min(pg + nb, pr + nb)
print(min(price))
