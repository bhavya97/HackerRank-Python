import re
for x in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print("False")
