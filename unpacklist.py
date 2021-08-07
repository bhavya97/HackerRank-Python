from PIL import Image

def avg(grades):
    first,*medium,last = grades
    avg = sum(medium)/ len(medium)
    print(avg)


avg( (57,68,78,44,33,85))

first = ["Bhavya","Girish","Deepak","Gaurav"]
last = ["Bhatia","Talreja","Sharma","Jadoun"]

names = zip(first,last)

for a,b in names:
    print(a,b)

print(first)
print(last)

stocks = {"Google":1058,"Yahoo":300,"Facebook":729,"Amazon":919,"Apple":768}

'''
stocks = {5:1058,4:300,3:729,1:919,2:768}

print(sorted(zip(stocks.values(),stocks.keys()))) 

for a,b in zip(stocks.values(),stocks.keys()):
    print(a,b)
'''

print(sorted(zip(stocks.values(),stocks.keys())))

for a,b in zip(stocks.values(),stocks.keys()):
    print(a,b)

img = Image.open("39.jpg")

print(img.size)
img.show()