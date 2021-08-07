from collections import Counter,OrderedDict

words=Counter([input() for _ in range(int(input()))])
print(len(words.items()))
print(*words.values())

words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())