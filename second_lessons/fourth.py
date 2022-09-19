from collections import Counter
words = [word for word in input().split(' ')]
map = dict(sorted(Counter(words).items(), key=lambda x: x[0]))
map_1 = dict(sorted(map))
print(map_1)
# for key, value in map.items():
#     print(key, value)
