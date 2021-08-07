income = [30,60,75]

def double_money(dollars):
    return dollars +dollars * 30/100

new_income = list(map(double_money,income))
print(new_income)

i = int(input())
tuple = []
for x in range(1,(i+1),1):
    tuple.append(x)

print(*tuple,sep="")



