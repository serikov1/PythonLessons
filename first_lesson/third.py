data = [float(elem) for elem in input().split(' ')]
if abs(data[0] - data[1]) * data[-1] > abs(data[0] - data[2]) * data[3] + abs(data[0] - data[1]) * data[3] + 3 * data[-2]:
    print('elevator')
else:
    print('stairs')