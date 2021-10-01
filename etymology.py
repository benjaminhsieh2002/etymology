from urllib.request import urlopen, Request
from decoder import languageDecoder

def wiktionaryLookup(word):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    try:
        data = urlopen(Request(url="https://en.wiktionary.org/wiki/"+word, headers=headers)).read()
    except:
        print("An error occured.")
        return 0
    data = data.decode("utf-8","replace")
    pos = data.find("<span class=\"mw-headline\" id=\"Etymology\">")
    etym = data[data.find("<p>", pos)+3:data.find("<h3>", pos)]
    while(etym.find("mention\" lang=")!=-1):
        code = etym[etym.find("lang=", etym.find("mention\" lang="))+6:etym.find(">", etym.find("mention\" lang="))-1]
        try:
            language = languageDecoder(code)
        except:
            #Code not found in languageDict, consider adding
            language = code
        print(language)
        etym = etym[etym.find("mention\" lang=")+1:]




while True:
    word = str(input("Enter Word (x to quit): ")).lower()
    if word == 'x':
        break
    else:
        wiktionaryLookup(word)
        print("\n")
