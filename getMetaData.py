# # coding: utf-8
# # 2018.08.23

# import requests
# import json
# import datetime

# def getMetaData():

# 	# detectWeatherKey = "日の天気は"

# 	# curlのオプションで指定している情報
# 	params = (
# 	  ('access_token', '103148b9423b6967c6e7971c091ea7ed657ede19d3d3a75ca6ae824ffb4cffb5'),
# 	)
# 	response = requests.get('https://api.bocco.me/alpha/rooms/09540d0d-ee72-455c-a248-accbe77ccac6/messages', params=params)
# 	#いくつかのメッセージを読み込む
# 	messages = response.json() #list


# 	# for i in range(len(messages)):
# 	# 	if messages[i]['text'].rfind(detectWeatherKey) > -1:
# 	# 		print(messages[i]['text'])
			

# 	# フォーマットの指定. ハイフンは0埋めしないためのやつ
# 	dateStr = datetime.datetime.today().strftime("%-m月%-d日")
# 	# weatherStr = 'はれ' #boccoのAPIから取得

# 	return dateStr, weatherStr


# if __name__ == "__main__":
#   getMetaData()