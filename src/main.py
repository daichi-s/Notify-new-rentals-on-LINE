import os
import sys
import re
import datetime
from bs4 import BeautifulSoup
sys.path.append('../')
import settings

import scraping
import linebot

# 対象ページを取得
scraping = scraping.Scraping()

listUrl = []
newUrlList = []

page = scraping.getPage(settings.SCRAPING_PAGE_URL)
aElems = scraping.getElement(page, 'a')

for a in aElems:
    try:
        aClass = a.get('class').pop(0)
        if aClass in 'js-cassette_link_href':
            listUrl.append(a.get('href'))
            print(listUrl)
    except:
        pass

# 更新日時をチェック、当日の場合は配列に格納
for url in listUrl:
    url = settings.SCRAPING_PAGE_DMAIN + url
    result = scraping.checkUpdateDate(url)

    if result:
        newUrlList.append(url)

    print(newUrlList)
##############################


linebot = linebot.Linebot()
text = linebot.createText(newUrlList)
res = linebot.pushMessage(settings.LINE_GROUP_ID, text)

