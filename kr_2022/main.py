# str = input()
# print('#'*(len(str) + 4))
# print('#', str, '#')
# print('#'*(len(str) + 4))


# #2
# def new_key(str):
#     return -len(str), str
#
# words = input().split()
# set_words = set()
# for elem in words:
#     set_words.add(elem)
# print(*sorted(set_words, key=new_key), sep='\n')

#3
M, N = [int(elem) for elem in input().split()]
field = []

for i in range(N):
    field.append(input())

field = [list(elem) for elem in field]
x, y, d = (int(elem) for elem in input().split())
for i in range(y-d, y+d+1):
    if 0 <= i < len(field):
        for j in range(x-d, x+d+1):
            if 0 <= j < len(field[i]):
                try:
                   print(field[i][j], end='')
                except:
                    continue
        print('\n', end='')

# for i in range(M):
#     for j in range(N):
#         try:
#             print(to_print[i][j], end='')
#         except:
#             continue
#     print('\n', end='')




# #4
# class Clock:
#     # Служебные методы, если нужны
#     def __init__(self):
#         self.time = [0, 0]
#
#     # Передвинуть время вперёд на minutes минут. Если minutes отрицательное - выбросить exception.
#     def tick(self, minutes):
#         if minutes < 0:
#             raise Exception
#         self.time[1] += minutes
#         self.time[0] += self.time[1] // 60
#         self.time[0] = self.time[0] % 24
#         self.time[1] = self.time[1] % 60
#
#
#     # Вернуть текущее время как tuple из часов и минут.
#     def get_time(self):
#         return (self.time[0], self.time[1])
#
# c = Clock()
# print(c.get_time())
# c.tick(60 * 23 + 15)
# print(c.get_time())

# #5
# try:
#     with open(input()) as f:
#         mas = f.readlines()
#     mas = [line.rstrip() for line in mas]
#     new_mas = []
#     for line in mas:
#         str = [int(elem) for elem in line.split()]
#         new_mas.append(str)
#     print(new_mas)
#     new_mas.sort()
#     max_size = [len(elem) for elem in new_mas]
#     print(max_size)
#     print(max(sum(elem) for elem in new_mas if len(elem) == max_size[0]))
#
# except:
#     print('0')

# m,n=map(int,input().split())
# pole=[]
# ans=[]
# for i in range(n):
#     a=input()
#     pole.append(a)
#     ans.append([0]*m)
# y,x,d=map(int,input().split())
# for i in range(x-d,x+d+1):
#     for j in range(y-d,y+d+1):
#         if i>=0 and j>=0 and i<=n and j<=m:
#             try:
#                 ans[i][j]=pole[i][j]
#             except:
#                 continue
# for x in ans:
#     while(0) in x:
#         x.remove(0)
#         a=''.join(x)
#     if a:
#         print(a)