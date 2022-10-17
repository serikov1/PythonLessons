# 1
# print(max((elem for elem in input().split('#')), key=len))

# 2
N, M = (int(elem) for elem in input().split())
quantity = int(input())
field = [[0] * M for i in range(N)]
for _ in range(quantity):
    x, y, r = (int(elem) for elem in input().split())
    for i in range(2 * r + 1):
        for j in range(2 * r + 1):
            try:
                field[x - r + i][y - r + j] = 1
            except:
                continue

print(field)
print(sum(elem.count(0) for elem in field))

