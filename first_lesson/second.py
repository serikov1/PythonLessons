int_nums = [int(elem) for elem in input().split(' ')]
int_nums.sort()
print(int_nums[-1] - int_nums[0])
