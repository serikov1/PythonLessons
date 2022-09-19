a, b = 0, 1
for i in range(int(input()) - 1):
    b, a = b + a, b
print(a)
