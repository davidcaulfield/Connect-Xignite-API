# This simple Python script demonstrates 
# making a simple rest call to
# XigniteG 
# It receives JSON data from the service.
# It parses and displays the data to the console
import requests
import json
import csv
from config import _token



base = "http://www.xignite.com/"

class Global_Historical:


	#make a get request to given url
	def getUrl(self, base, path, **kwargs):
		params = dict(_token=_token)
		params.update(kwargs["params"])
		response = requests.get(base + path, params=params)
		if response.status_code in range(200,300):
			return response.json()
		else:
			return {
				"status_code": response.status_code,
				"text": response.text 
			}


	def end_of_day_quote(self, base, params):
		path = "xGlobalHistorical.json/GetEndOfDayQuote"
		response = self.getUrl(base, path, params=params)
		print(response)
		price, change, volume = response['LastClose'], response['ChangeFromLastClose'], response['Volume']
		return price, change, volume


params = dict(
	IdentifierType="Symbol",
	Identifier="SPYX",
	AdjustmentMethod="SplitAndProportionalCashDividend",
	EndOfDayPriceMethod="LastTrade",
	AsOfDate="03/19/2017",
	_fields=[
		"Security.Symbol","Date","Volume",
		"LastClose","ChangeFromLastClose",
		"PercentChangeFromLastClose"
	],
	_token=_token
)


sp = Global_Historical()
print(sp.end_of_day_quote(base, params))