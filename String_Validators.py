str = input()
print(any(c.isalnum()  for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))
list = [1,2,3,4]
print(any(a == 5 for a in list))
