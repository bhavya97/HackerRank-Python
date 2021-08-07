myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(),key=myList.index),sep="")
#print(*sorted(input(),key = lambda x: (x.isdigit(),x.isdigit() and int(x)%2==0,x.isupper(),x.islower(),x)),sep="")
#print(*sorted(input(), key = lambda x :(0 if x.islower() else 1 if x.isupper() else 2 if int(x)%2!=0 else 3)),sep='')
