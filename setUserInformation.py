# coding: utf-8
# 2018.08.28

import requests
import json
import uuid


def setUserInformation():
  api_key = '4QiLD9c9Qr8IDJE7ALqX6wpAaKPUNGrf69xfTMCO2a9T9MRiHw4BpA5fHjG6KbOE' #宮西のAPI KEY
  email= 'miyanishi56@gmail.com' # 宮西のemail
  password = '3910yuka' #宮西のパスワード


  ###############################
  # API KEYからACCESS TOKEN取得
  ###############################
  data = [
    ('apikey', api_key),
    ('email', email),
    ('password', password),
  ]
  response = requests.post('https://api.bocco.me/alpha/sessions', data=data)
  responseJson = response.json()
  accessToken = responseJson['access_token']
  print("> ACCESS TOKEN was succusessfully generated. :" + accessToken)

  
  ###############################
  # API KEYからROOMのUUID取得
  ###############################
  params = (
      ('access_token', accessToken),
  )
  response = requests.get('https://api.bocco.me/alpha/rooms/joined', params=params)
  responseJson = response.json()
  roomUuid = responseJson[0]['uuid']
  print("> ROOM UUID was succusessfully generated. :" + roomUuid)


  ###############################
  # 取得したACCESS TOKENと
  # API KEYをファイルに保存
  ###############################
  with open('data/userInfo.txt', mode='w') as f:
    f.write(str(accessToken + '\n' + roomUuid))



if __name__ == "__main__":
  setUserInformation()
