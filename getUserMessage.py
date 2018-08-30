# coding: utf-8
# 2018.08.22

import requests
import json
import detectUserMessage as detectUsrMsg
import random

def getUserMessage():

  userMessage = ""
  detectWeatherKey = "の天気は"
  weatherNum = 1 # default 0,1,2

  if detectUsrMsg.detectUserMessage():
    # curlのオプションで指定している情報
    params = (
      ('access_token', '103148b9423b6967c6e7971c091ea7ed657ede19d3d3a75ca6ae824ffb4cffb5'),
    )

    response = requests.get('https://api.bocco.me/alpha/rooms/09540d0d-ee72-455c-a248-accbe77ccac6/messages', params=params)
    #いくつかのメッセージを読み込む
    messages = response.json() #list
    
    #最新のメッセージを読み込む
    # 何回かリクエストを送ってるとたまにlistじゃなくてdictで帰ってくる時がある(中身はエラーメッセージ?未確認)
    # その例外処理を無理やり書いておく
    if(isinstance(messages, list)):

      # usrMessageのリクエストを送ったとき、userMesssage以外にも、
      # ついでに天気をここで取得しておく
      for i in range(len(messages)):
        msgTxt = messages[i]["text"]
        if msgTxt.find(detectWeatherKey) > -1:
          msgTxt = msgTxt[msgTxt.find(detectWeatherKey):]
          
          if msgTxt.find('晴') > -1:
            weatherNum = 0
          elif msgTxt.find('曇') > -1:
            weatherNum = 1
          elif msgTxt.find('雨') > -1:
            weatherNum = 2

          # デモ用
          weatherNum = random.randrange(3)

        # else:
          # print("> Weather does not be found.")

        # print(msgTxt)
        # print("weatherNum: " + str(weatherNum))



      print("...")
      latestUserMsg = messages[len(messages)-1] # dictlatestUserMsg = messages[len(messages)-1] #dict
      
      # 指定されたユーザだったら
      # if latestUserMsg["user"]["uuid"] == designatedUserUUID:
      userMessage = latestUserMsg["text"] + '。' # 最後に句点入れておく
      userMessage = userMessage.replace(' ', '。') # スペースがあったら句点に置換
      
      return userMessage, weatherNum


    else:
      print("> User message does not found.")
      return userMessage, weatherNum


    print( '> Got {' + str(userMessage) + '} from bocco server.')



    



if __name__ == "__main__":
    getUserMessage()