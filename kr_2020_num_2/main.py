# # 1
# N = int(input())
# data = []
# for i in range(N):
#     mas = tuple(int(elem) for elem in input().split())
#     data.append(mas)
#
# mas = dict(data)
# print(*({k: v for k, v in sorted(mas.items(), key=lambda item: item[1], reverse=True)}.keys()), sep='\n')


# # 2
# mas = [elem for elem in input().split()]
# if len(mas) != 3 or (not((mas[0] or mas[2]).isdigit()) and (mas[0] or mas[2]).startswith('-') and not((mas[0][1] or mas[2][1]).isdigit())) or (not((mas[0] or mas[2]).isdigit()) and not(mas[0] or mas[2]).startswith('-')):
#     print('Bad input')
# elif mas[1] == '*':
#     print(int(mas[0]) * int(mas[2]))
# elif mas[1] == '^':
#     print(int(mas[0]) ** int(mas[2]))
# elif mas[1] == '-':
#     print(int(mas[0]) - int(mas[2]))
# elif mas[1] == '+':
#     print(int(mas[0]) + int(mas[2]))


# # 3
# x = [float(elem) for elem in input().split()]
# y = [float(elem) for elem in input().split()]
# z = [float(elem) for elem in input().split()]
#
# N = int(input())
# coords = []
# for i in range(N):
#     coord = [float(elem) for elem in input().split()]
#     coords.append(coord)
#
# counter = 0
# for elem in coords:
#     if x[0] <= elem[0] <= x[1] and y[0] <= elem[1] <= y[1] and z[0] <= elem[2] <= z[1]:
#         counter += 1
#
# print(counter)

# 4
# N = int(input())
# values = {}
# for i in range(N):
#     mas = [float(elem) for elem in input().split()]
#     values[mas[0]] = mas[1]
#
# pressure = 0
# p_count = 0
# temp = 0
# for key, value in values.items():
#     temp += key
#     if -70 < key < 80:
#         pressure += value
#         p_count += 1
#
# print(f'{float(temp)/len(values):.4f}', f'{float(pressure)/p_count:.4f}')

#5
with open(input(), 'r') as f:
    f.read()
