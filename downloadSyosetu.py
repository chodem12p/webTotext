from selenium import  webdriver
from webdriver_manager.chrome import  ChromeDriverManager


def webToText():
    browser.get(link)
    text=browser.find_elements_by_tag_name("p")
    print("loading website:"+link)
    for i in text[:-7]:
        textfile.write(i.text+"\n")
        if (i.text+"" =="data　───────────"):
            textfile.write("break\n")
            print("break "+i.text)
            break
    print("finsin")
#123
def UIinput():
    #https://ncode.syosetu.com/n9572he/1/
    link =input("小說網址:")
    toPage = int(input("至幾頁:"))
    return link,toPage

webOptions = webdriver.ChromeOptions()
webOptions.add_argument('headless')
browser =webdriver.Chrome(ChromeDriverManager().install(),options=webOptions)
endPage = None
toPage=0
link = ""

while True:
    link,toPage=UIinput()
    lstr = str.split(link, "/")
    n = -1
    while True:
        if (lstr[n] != ""):
            break
        n -= 1
    if endPage is None:
        endPage=int(lstr[n])+toPage+1

    with open(lstr[n-1]+"-"+lstr[n]+"-"+str(endPage-1)+".text","w",encoding="utf-8") as textfile:
        pagelist=range(int(lstr[n]),endPage)
        for ind in pagelist:
            lstr[n]=str(ind)
            link = ""
            for i in lstr:
                link += (i + "/")
            webToText()
    endPage = None
    print("All finsin")