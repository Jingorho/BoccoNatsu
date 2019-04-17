# coding: utf-8
# 2018.08.22

import requests
import json
import detectUserMessage as detectUsrMsg
import getUserInformation as getUserInfo
import setTheme as setTm
import random

def getUserMessage(detectedUserMessageNum):
  userInfo = getUserInfo.getUserInformation() # access_token, room_uuidが帰ってくる

  userMessage = ""
  detectWeatherKey = "の天気は"
  weatherNum = 1 # default 0,1,2
  setThemeTrigger1 = "テーマは"
  setThemeTrigger2 = "お題は"

  # 引数で取るようにしたので不要
  # detectedUserMessageNum = detectUsrMsg.detectUserMessage()

  
  # 1: トリガーを含まない, 2: テーマ設定を含む, 3: 開始トリガーを含む 
  if detectedUserMessageNum > 0:
    params = ( ('access_token', userInfo[0]), )
    response = requests.get('https://api.bocco.me/alpha/rooms/'+ userInfo[1] +'/messages', params=params)
    #いくつかのメッセージを読み込む
    messages = response.json() #list
    
    # いくつかのメッセージ列の中から最新のメッセージを読み込む
    # 何回かリクエストを送ってるとたまにlistじゃなくてdictで帰ってくる時がある(中身はエラーメッセージ?未確認)
    # その例外処理を無理やり書いておく
    if(isinstance(messages, list)):

      # usrMessageのリクエストを送ったとき、userMesssage以外にも、
      # ついでに天気をここで取得しておく
      for i in range(len(messages)):
        msgTxt = messages[i]['text']
        if msgTxt.find(detectWeatherKey) > -1:
          msgTxt = msgTxt[msgTxt.find(detectWeatherKey):]
        
          if msgTxt.find('晴') > -1:
            weatherNum = 0
          elif msgTxt.find('曇') > -1:
            weatherNum = 1
          elif msgTxt.find('雨') > -1:
            weatherNum = 2

        # else:
          # print("> Weather does not be found.")

      print("...")

      latestUserMsg = messages[len(messages)-1] # dictlatestUserMsg = messages[len(messages)-1] #dict

    

      # テーマ設定のトリガーを含むメッセージだったら
      if detectedUserMessageNum is 2:
        userMessage = latestUserMsg["text"]

        if latestUserMsg["text"].find(setThemeTrigger1) > -1:
          userMessage = userMessage[userMessage.find(setThemeTrigger1)+len(setThemeTrigger1):] #メッセージの中からテーマを抽出
        
        else :
          userMessage = userMessage[userMessage.find(setThemeTrigger2)+len(setThemeTrigger2):] #メッセージの中からテーマを抽出
        
        print("> {" + userMessage + "}")

      # セッション開始のトリガーを含むメッセージだったら
      # if detectedUserMessageNum is 3:
        # 処理はなにもない

      # トリガーを含まないメッセージだったら
      else:
        # if latestUserMsg["user"]["uuid"] == designatedUserUUID: # 指定されたユーザだったら
        userMessage = latestUserMsg["text"] + '。' # 最後に句点入れておく
        # userMessage = userMessage.replace(' ', '。') # スペースがあったら句点に置換

    # if(isinstance(messages, list))

  else:
    print("> User message does not found.")
  

  # if detectedUserMessageNum > 0:



  # デモ用に乱数で上書き
  weatherNum = random.randrange(3)
  print( '> Got {' + str(userMessage) + '} from bocco server.')
  return userMessage, weatherNum

  



if __name__ == "__main__":
  getUserMessage()