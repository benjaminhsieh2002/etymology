from urllib.request import urlopen, Request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
word = str(input("Enter Word: ")).lower()
try:
    data = urlopen(Request(url="https://en.wiktionary.org/wiki/"+word, headers=headers)).read()
except:
    print("An error occured.")
    exit()
data = data.decode("utf-8","replace")
pos = data.find("<span class=\"mw-headline\" id=\"Etymology\">")
etym = data[data.find("<p>", pos)+3:data.find("<h3>", pos)]
while(etym.find("mention\" lang=")!=-1):
    print(etym[etym.find("lang=", etym.find("mention\" lang="))+6:etym.find(">", etym.find("mention\" lang="))-1])
    etym = etym[etym.find("mention\" lang=")+1:]