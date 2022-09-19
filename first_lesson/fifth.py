num = int(input())
amount = [int(elem) for elem in str(num)]
while len(amount) > 1:
    suma = sum(amount)
    amount = [int(elem) for elem in str(suma)]

print(*amount)

