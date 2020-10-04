# import os
import requests
import re
import datetime
from bs4 import BeautifulSoup

class Scraping:

    # Webページをスクレイピングして取得
    def getPage(self, url):
        res = requests.get(url)
        result = BeautifulSoup(res.text, 'html.parser')
        return result

    # スクレイピングしたページの対象要素を取得
    def getElement(self, page, tag):
        return page.html.body.find_all(tag)


    # 更新日時が当日かをチェック
    def checkUpdateDate(self, url):
        page = self.getPage(url)
        divElems = self.getElement(page, 'div')

        for elem in divElems:
            try:
                classElem = elem.get('class').pop(0)
                if classElem in 'captiontext':
                    classElem = elem.get('class').pop(0)
                    if classElem in 'l-space_medium':
                        date = re.search(r'\d{4}/\d{1,2}/\d{1,2}', elem.string).group()
                        today = datetime.date.today()
                        publishedDatetime = datetime.datetime.strptime(date.replace('/', '-'), '%Y-%m-%d')
                        publishedDate = datetime.date(publishedDatetime.year, publishedDatetime.month, publishedDatetime.day)

                        result = False
                        if today == publishedDate:
                            result = True
                        
                        return result
            except:
                pass
