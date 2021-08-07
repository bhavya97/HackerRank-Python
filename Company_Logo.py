from collections import Counter
[print(*i) for i in Counter(sorted(input())).most_common(3)]

'''
from collections import Counter
a = Counter(sorted(input())).most_common(3)
print("{} {}\n{} {}\n{} {}".format(*a[0],*a[1],*a[2]))
'''