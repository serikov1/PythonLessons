links = input().split()
words = set()
for link in links:
    try:
        with open(link, 'r') as f:
            for elem in f.read().split():
                words.add(elem)
    except:
        continue
print(*sorted(words))
