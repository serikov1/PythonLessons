from numpy import array, unique

# 1
# data = [int(elem) for elem in input().split()]
# data = [i for i in data if data.count(i) == 1]
# print(max(data))

# 2
# words = [elem for elem in input().split()]
# map = {}
#
# for elem in unique(words):
#     map.update({elem: words.count(elem)})
#
# data = sorted(map.items(), key=lambda kv: kv[1], reverse=True)
# for elem in data:
#     print(elem[1], elem[0])

# 3
# data = [int(elem) for elem in input().split()]
# percentile = int(input())
# amount = len(data) * percentile / 100
# if (amount * 10) % 10 != 0:
#     amount = int(amount) + 1
# print(sorted(data)[int(amount) - 1])

#4
# N = int(input())
# data = array([array([float(i) for i in input().split()]) for s in range(N)])
#
# stuff = dict()
# for row in range(N):
#     for elem in range(7):
#         if elem == 1:
#             try:
#                 stuff[int(data[row][1])].append(data[row][5])
#             except:
#                 activity = []
#                 stuff.update({int(data[row][1]): activity})
#                 stuff[int(data[row][1])].append(data[row][5])
# to_print = dict()
# for key in stuff:
#     if len(stuff[key]) > 1:
#         to_print[key] = max(stuff[key]) - min(stuff[key])
# to_print = sorted(to_print.items(), key=lambda kv: kv[1])
# keys = stuff.keys()
# print(to_print)
# try:
#     if len(to_print) > 2:
#         for key in range(3):
#             id, da = to_print[key]
#             print(id, end=' ')
#     else:
#         id, da = to_print[0]
#         print(id, end=' ')
# except:
#     print('-1')

#5
# dim = int(input())
# r0 = [float(elem) for elem in input().split()]
# S = array([array([float(i) for i in input().split()]) for s in range(dim)])
# k = int(input())
# r = r0
# for i in range(k):
#     r = S @ r
# for elem in range(len(r)):
#     print(f'{r[elem]:.4f}', end=' ')
