from urllib import request

def pizza():
    print("Hi !!! i am a pizza")

url = "http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv"
request.urlretrieve(url,"data.csv")

def download_stock_data(csv_url):

    response = request.urlopen(csv_url)
    print(response.read())
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'stock.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(url)

def open_csv():
    fx = open("C2ImportCalEventSample.csv","r")
    content = fx.read()
    print(content)

open_csv()

print(r"hello\nworld")
'''r causes the special character to be interpreted as actual backslashesh '''
print("hello\nworld")