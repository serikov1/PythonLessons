# data = [elem.lower() for elem in input().split()]
# data_set = set(data)
# print(len(data_set))

# #2
# from numpy import array, zeros
#
# N, M = (int(elem) for elem in input().split())
# k = int(input())
#
# data = array([array([int(i) for i in input().split()]) for _ in range(k)])
# field = zeros((M, N))
# for elem in data:
#     field[elem[0], :] += 1
#     field[:, elem[1]] += 1
#     field[elem[0], elem[1]] -= 1
# print(field)
# result = 0
# for i in range(M):
#     for j in range(N):
#         if field[i][j] > 1:
#             result += 1
#
# print(result)

# #3
# from numpy import array
# from math import sqrt
# N = int(input())
# data = array([array([float(i) for i in input().split()]) for _ in range(N)])
# print(data)
# x = 0
# y = 0
# result = [0, 0]
# for elem in data:
#     x = elem[2]/sqrt(elem[0]**2 + elem[1]**2)
#     y = elem[2]/sqrt(elem[0]**2 + elem[1]**2)
#     elem[0] *= x
#     elem[1] *= y
#     result[0] += elem[0]
#     result[1] += elem[1]
# print(data)
# print(f'{result[0]:.4f}', f'{result[1] :.4f}')


# from math import sqrt
# n = int(input())
#
# f = []
# for i in range(n):
#     f.append([float(it) for it in input().split()])
# print(f)
# for i in range(n):
#     x = f[i][0]
#     f[i][0] *= (f[i][2] / sqrt(f[i][0]**2 + f[i][1]**2))
#     f[i][1] *= (f[i][2] / sqrt(x**2 + f[i][1]**2))
#
# x0 = [0, 0]
#
# for i in range(n):
#        x0[0] += f[i][0]
#        x0[1] += f[i][1]
#
# print(f)
# for i in x0:
#     print('%.4f' % i, end=' ')

# #4
# sum = 0
# data1 = [elem.lower() for elem in input().split(',')]
# data2 = [elem.lower() for elem in input().split(',')]
# # print(data1[0], data2, sep='\n')
# if len(data1) == len(data2):
#     for elem in data1:
#         if elem in data2:
#             sum += 1
#     if sum == len(data1):
#         print('equal')
#     else:
#         print('different')
# else:
#     print('different')

# # 5
# from PIL import Image
# from numpy import array, dot, min, max
#
# # считаем картинку в numpy array
# ref = input()
# img = Image.open(ref)
# data = array(img)
# rgb = data[:, :, :3]
# transform_to_wb = array([0.299, 0.587, 0.114])
# wb_image = dot(rgb, transform_to_wb)
# print(int(min(wb_image)), int(max(wb_image)))

#8
from numpy import array, delete
N = int(input())
data = array([array([i for i in input().split()]) for _ in range(N)])
for i in range(N):
    if not data[i][-2].isalnum() or len(data[i][-2])>6:
        delete(data, data[i])
