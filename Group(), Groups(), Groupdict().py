import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m)