def primenumber(x, y):
    for b in range(x ,y):
        if x == 0:
            continue
    primenumberList = [i for i in range(2, y + 1) if all(i % j for j in range(2, i))]
    print(primenumberList)


primenumber(0, 100)