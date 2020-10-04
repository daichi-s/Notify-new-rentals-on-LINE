import os
import requests
import json
import datetime

class Linebot:

    LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
    LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

    def getHeader(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.BEARER_TOKEN,
        }
        return headers

    def pushMessage(self, to, text):
        endpoint = 'https://api.line.me/v2/bot/message/push'
        payload = {
	        "to": to,
	        "messages": [
		        {
                    "type": "text",
                    "text": text
                }
	        ],
        }
        return requests.post(endpoint, json.dumps(payload), headers=self.getHeader())

    def createText(self, listUrl):
        today = datetime.date.today().strftime('%Y年%m月%d日')

        if not listUrl:
            return today + 'の新着情報はありません。'

        template = today + 'の新着情報をお届けします。'
        urls = '\r\n'.join(listUrl)
        return template + '\r\n' + urls
