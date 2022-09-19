N = int(input())
nums = [int(input()) for i in range(N)]
nums_plus = []
nums_minus = []
nums_null = []
for elem in nums:
    if elem > 0:
        nums_plus.append(elem)
    elif elem < 0:
        nums_minus.append(elem)
    elif elem == 0:
        nums_null.append(elem)
sort = []
for elem in sorted(nums_null):
    sort.append(elem)
for elem in sorted(nums_plus):
    sort.append(elem)
for elem in sorted(nums_minus, reverse=True):
    sort.append(elem)
print(*sort)
