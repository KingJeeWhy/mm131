import requests
import os
from bs4 import BeautifulSoup


def getHtml(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
               "Referer": "https://www.mm131.net"
        }
    html = requests.get(url, headers = headers)
    html.encoding = html.apparent_encoding
    return html


def getSoup(html):
    return BeautifulSoup(html.text, "html.parser")


def getTitle(soup):
    title = soup.title.contents[0]
    return str(title)


def getAllPage(soup):
    allPage = soup.select('body > div.content > div.content-page > span:nth-child(1)')[0].string[1:-1]
    return allPage


def makedir(title):
    try:
        os.mkdir(title)
    except:
        print(f"{title} folder is exist!")
        return


def downloadPic(title, allPage, htmlMark):
    for number in range(1,int(allPage)+1):
        picUrl = f"https://img1.mmmw.net/pic/{htmlMark}/{number}.jpg"
        pic = getHtml(picUrl)
        with open(f"{title}/{number}.jpg", "wb+") as f:
            f.write(pic.content)
            print(f"{number}.jpg download successful!")



def main():
    for mark in range(4000,4005):
        htmlMark = str(mark)
        try:
            html = getHtml(f"https://www.mm131.net/xinggan/{htmlMark}.html")
            soup = getSoup(html)
            title = getTitle(soup)
            allPage = getAllPage(soup)
            makedir(title)
        except:
            continue
        downloadPic(title, allPage, htmlMark)


if __name__ == '__main__':
    main()

