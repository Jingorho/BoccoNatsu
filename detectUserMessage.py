# coding: utf-8
# 2018.08.22

import requests
import json
import getUserInformation as getUserInfo

def detectUserMessage():
  userInfo = getUserInfo.getUserInformation() # access_token, room_uuidが帰ってくる

  startTriggerWord = "おはよう"
  detectedMessageType = 0 # 0は発見できていない、1は最初のお題をスタートするトリガ、2は写真のupを検知するトリガ

  # 子供のUUIDを指定するならここに入力. 今の所は「BOCCOのUUID以外だったら」にしておく
  # designatedUserUUID = "33e739e3-b6f0-4ab8-9824-3fde9f6e7827"
  boccoUUID = "33e739e3-b6f0-4ab8-9824-3fde9f6e7827"

  # curlのオプションで指定している情報
  params = (
    ('access_token', userInfo[0]),
  )
  response = requests.get('https://api.bocco.me/alpha/rooms/'+userInfo[1]+'/messages', params=params)
  messages = response.json() #list

  # 最新のメッセージを読み込む
  # 何回かリクエストを送ってるとたまにlistじゃなくてdictで帰ってくる時がある。
  # その例外処理を無理やり書いておく
  if(isinstance(messages, list)):
    
    print("...")
    latestUserMsg = messages[len(messages)-1] #dict

    # 指定されたユーザ(子供)だったら
    # if latestUserMsg["user"]["uuid"] == designatedUserUUID:
    # もしくは
    # BOCCO以外のユーザだったら
    if latestUserMsg["user"]["uuid"] != boccoUUID:

      ###############################
      # スタートのトリガーのワード「おはよう」を含んでいたら
      ###############################
      if latestUserMsg["text"].find(startTriggerWord) > -1:
        detectedMessageType = 1
        print('> Detected user message including ' + startTriggerWord + '.')
      

      ###############################
      # それ以外のメッセージだったら
      ###############################
      else:
        detectedMessageType = 2
        print('> Detected user message.')
    

    return detectedMessageType
    # if BOCCO以外のユーザだったら





  else:
    print(messages)
    print(len(messages))
    print(type(messages))
    return detectedMessageType
  # listじゃなくてdictで帰ってくる時のための例外処理



if __name__ == "__main__":
    detectUserMessage()

