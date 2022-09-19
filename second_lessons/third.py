from collections import Counter
mas = [int(n) for n in input().split(' ')]
repeat = [elem for elem, count in Counter(mas).items() if count > 1]

print(max(mas[i] for i, no_rep in enumerate(mas) if no_rep not in repeat))