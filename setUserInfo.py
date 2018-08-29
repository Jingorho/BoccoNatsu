# coding: utf-8
# 2018.08.28

import requests
import json
import bocco


api = bocco.api.Client('535f77f09d7f6da5da9ab11885302d7885720d7b437efe06cf3f4b096406df45')
room_uuid = uuid.UUID('09540d0d-ee72-455c-a248-accbe77ccac6')


def setUserInfo():
  api_key = '4QiLD9c9Qr8IDJE7ALqX6wpAaKPUNGrf69xfTMCO2a9T9MRiHw4BpA5fHjG6KbOE' #宮西のAPI KEY
  email= 'miyanishi56@gmail.com' # 宮西のemail
  password = '3910yuka' #宮西のパスワード

  response = api.signin(api_key, email, password)
  
  print(response)


if __name__ == "__main__":
  setUserInfo()
