# coding: utf-8
# 2018.08.22

import random
import os

def getBoccoMessage(typeNum):
  # typeNum = 2

  # typeNum: 1は"今日は何を取ったの", 2は"へーそうなんだ"
  
  path = 'data/boccoMsgDB_' + str(typeNum) + '.txt'

  if os.path.exists(path):
    with open(path) as f:
      fileContents = f.read()
      messages = fileContents.split("\n")

      boccoMessage = messages[random.randrange(len(messages))]

      if typeNum is 2:
        boccoMessage = boccoMessage + 'GoogleDriveにアップロードしたよ'

      print( '> {' + str(boccoMessage) + '} was returned.')

      return boccoMessage
  
  else:
    print('> {' + path + '} does not be found.')

  

if __name__ == "__main__":
  getBoccoMessage()